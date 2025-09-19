import ast
from pathlib import Path

from pypp_cli.src.transpilers.library.transpiler.d_types import (
    ModulePyImports,
    QInc,
)
from pypp_cli.src.transpilers.library.transpiler.cpp_includes import IncMap
from pypp_cli.src.transpilers.library.transpiler.util.modules import (
    calc_module_beginning,
)


# TODO: simplify this code.
def analyse_import_stmts(
    stmts: list[ast.stmt],
    py_modules: set[str],
    namespace: str | None,
    lib_namespaces: dict[str, str],
    file_path: Path,
) -> tuple[IncMap, int, ModulePyImports, dict[str, str]]:
    i = 0
    # This one contains a map of import name to the required CppInclude, so that when
    # I find the name is used in the file, I add the CppInclude.
    cpp_inc_map: IncMap = {}
    # This one is a data structure containing all the python imports in the file. I use
    # it when I need to check if something is imported or not.
    module_py_imports = ModulePyImports({}, set())
    # This one is not a set of names to the namespace they belong to.
    namespaces: dict[str, str] = {}
    for i, node in enumerate(stmts):
        if isinstance(node, ast.ImportFrom):
            if node.module in module_py_imports.imp_from:
                raise ValueError(
                    f"Duplicate import from module not supported. "
                    f"module: {node.module}. In {file_path}"
                )
            if node.module is None:
                raise ValueError(
                    "Import with just a '.' not supported. Problem in {file_path}"
                )
            if node.module in py_modules or _is_pure_lib(node.module, lib_namespaces):
                inc: QInc = QInc.from_module(node.module)
                for alias in node.names:
                    assert alias.asname is None, (
                        f"'as' is not supported in import from. In {file_path}"
                    )
                    cpp_inc_map[alias.name] = inc
            if node.module in py_modules:
                for alias in node.names:
                    namespaces[alias.name] = (
                        namespace if namespace is not None else "me"
                    )
            lib = calc_module_beginning(node.module)
            if lib in lib_namespaces:
                for alias in node.names:
                    namespaces[alias.name] = lib_namespaces[lib]
            module_py_imports.imp_from[node.module] = [n.name for n in node.names]
        elif isinstance(node, ast.Import):
            raise ValueError(
                f"Import is not supported in Py++ "
                f"(only ImportFrom is supported).\nProblem file:\n{file_path}"
            )
        else:
            break
    return cpp_inc_map, i, module_py_imports, namespaces


def _is_pure_lib(module: str, lib_namespaces: dict[str, str]) -> bool:
    # For all pure libs, there is a key in the lib_namespaces dict.
    return calc_module_beginning(module) in lib_namespaces
