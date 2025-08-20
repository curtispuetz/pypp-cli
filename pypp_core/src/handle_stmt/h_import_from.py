import ast

from pypp_core.src.d_types import QInc
from pypp_core.src.util.ret_imports import IncMap


_DISALLOWED_SET: set[str] = {
    "typing",
    "dataclasses",
    "collections",
    "abc",
    "pypp_python",
}


def handle_import_from(node: ast.ImportFrom, proj_info: dict, cpp_inc_map: IncMap):
    assert node.module is not None, "Not supported"
    assert node.level == 0, "Only absolute import supported"
    # NOTE: a hack for now.
    # TODO: for bridge libraries, you should be able to specify modules to ignore here.
    if node.module == "pypp_bridge_library_test_0.pseudo_custom_type":
        print("here")
    b = _calc_module_beginning(node.module)
    if b in _DISALLOWED_SET or b in proj_info["installed_libraries"]:
        return
    module_str = node.module.replace(".", "/") + ".h"
    for alias in node.names:
        assert alias.asname is None, "'as' is not supported in import from"
        cpp_inc_map[alias.name] = QInc(module_str)


def _calc_module_beginning(module: str) -> str:
    f = module.find(".")
    if f == -1:
        return module
    return module[:f]
