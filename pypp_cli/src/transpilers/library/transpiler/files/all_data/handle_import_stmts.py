import ast
from pathlib import Path

from pypp_cli.src.transpilers.library.transpiler.d_types import (
    ModulePyImports,
    PyImport,
    QInc,
)
from pypp_cli.src.transpilers.library.transpiler.maps.maps import Maps
from pypp_cli.src.transpilers.library.transpiler.cpp_includes import IncMap
from pypp_cli.src.transpilers.library.transpiler.util.modules import (
    calc_module_beginning,
)


# TODO: simplify this code.
def analyse_import_stmts(
    stmts: list[ast.stmt],
    maps: Maps,
    py_modules: set[str],
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
    # This one is a set of names that are imported from the users project itself. I use
    # this to know if I should add the "me" namespace or not.
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
            if node.module in py_modules or maps.import_.contains(node.module):
                inc: QInc = _calc_q_inc(node.module)
                for alias in node.names:
                    assert alias.asname is None, (
                        f"'as' is not supported in import from. In {file_path}"
                    )
                    cpp_inc_map[alias.name] = inc
            if node.module in py_modules:
                for alias in node.names:
                    namespaces[alias.name] = "me"
            lib = calc_module_beginning(node.module)
            if lib in lib_namespaces:
                for alias in node.names:
                    namespaces[alias.name] = lib_namespaces[lib]
            module_py_imports.imp_from[node.module] = [n.name for n in node.names]
        elif isinstance(node, ast.Import):
            for name in node.names:
                if name.name in py_modules:
                    raise ValueError(
                        "Import is not supported for project imports "
                        "(only ImportFrom is supported). In {file_path}"
                    )
                if maps.import_.contains(name.name):
                    assert name.asname is not None, (
                        f"import 'as' required for {name.name}. In {file_path}"
                    )
                    cpp_inc_map[name.asname] = _calc_q_inc(name.name)
                module_py_imports.imp.add(PyImport(name.name, name.asname))
        else:
            break
    return cpp_inc_map, i, module_py_imports, namespaces


# TODO: extract this function.
def _calc_q_inc(name: str) -> QInc:
    return QInc(name.replace(".", "/") + ".h")
