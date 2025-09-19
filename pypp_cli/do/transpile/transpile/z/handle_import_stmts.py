import ast
from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.transpile.z_i.d_types import (
    ModulePyImports,
    QInc,
)
from pypp_cli.do.transpile.transpile.z_i.cpp_includes import IncMap


type _Result = tuple[IncMap, int, ModulePyImports, dict[str, str]]


def analyse_import_stmts(
    stmts: list[ast.stmt],
    py_modules: set[str],
    namespace: str,
    lib_namespaces: dict[str, str],
    file_path: Path,
) -> _Result:
    # This one contains a map of import name to the required CppInclude, so that when
    # I find the name is used in the file, I add the CppInclude.
    cpp_inc_map: IncMap = {}
    # This one is a data structure containing all the python imports in the file. I use
    # it when I need to check if something is imported or not.
    module_py_imports = ModulePyImports({}, set())
    # This one is not a set of names to the namespace they belong to.
    namespaces: dict[str, str] = {}
    analyzer = _ImportStmtAnalyzer(
        stmts,
        py_modules,
        namespace,
        lib_namespaces,
        file_path,
        cpp_inc_map,
        module_py_imports,
        namespaces,
    )
    return analyzer.analyse()


@dataclass
class _ImportStmtAnalyzer:
    _stmts: list[ast.stmt]
    _py_modules: set[str]
    _namespace: str
    _lib_namespaces: dict[str, str]
    _file_path: Path
    _cpp_inc_map: IncMap
    _module_py_imports: ModulePyImports
    _namespaces: dict[str, str]

    def analyse(self) -> _Result:
        i = 0
        for i, node in enumerate(self._stmts):
            if isinstance(node, ast.ImportFrom):
                if node.module is None:
                    raise ValueError(
                        "Import with just a '.' not supported. Problem in {file_path}"
                    )
                self._update_cpp_inc_map(node.module, node.names)
                self._update_namespaces(node.module, node.names)
                self._update_module_py_imports(node.module, node.names)
            elif isinstance(node, ast.Import):
                raise ValueError(
                    f"Import is not supported in Py++ "
                    f"(only ImportFrom is supported).\nProblem file:\n{self._file_path}"
                )
            else:
                break
        return self._cpp_inc_map, i, self._module_py_imports, self._namespaces

    def _update_cpp_inc_map(self, module: str, names: list[ast.alias]):
        if module in self._py_modules or self._is_pure_lib(module):
            inc: QInc = QInc.from_module(module)
            for alias in names:
                assert alias.asname is None, (
                    f"'as' is not supported in import from. In {self._file_path}"
                )
                self._cpp_inc_map[alias.name] = inc

    def _update_namespaces(self, module: str, names: list[ast.alias]):
        if module in self._py_modules:
            for alias in names:
                self._namespaces[alias.name] = self._namespace
        lib = _calc_module_beginning(module)
        if lib in self._lib_namespaces:
            for alias in names:
                self._namespaces[alias.name] = self._lib_namespaces[lib]

    def _update_module_py_imports(self, module: str, names: list[ast.alias]):
        name_strs = [n.name for n in names]
        if module in self._module_py_imports.imp_from:
            self._module_py_imports.imp_from[module].extend(name_strs)
        else:
            self._module_py_imports.imp_from[module] = name_strs

    def _is_pure_lib(self, module: str) -> bool:
        # For all pure libs, there is a key in the _lib_namespaces dict.
        return _calc_module_beginning(module) in self._lib_namespaces


def _calc_module_beginning(module: str) -> str:
    f = module.find(".")
    if f == -1:
        return module
    return module[:f]
