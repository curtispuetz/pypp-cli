import ast

from src.d_types import QInc
from src.util.ret_imports import ImpMap


def handle_import_from(node: ast.ImportFrom, imp_map: ImpMap):
    assert node.module is not None, "Not supported"
    assert node.level == 0, "Only absolute import supported"
    # NOTE: a hack for now.
    # TODO: for bridge libraries, you should be able to specify modules to ignore here.
    if node.module in {
        "typing",
        "dataclasses",
        "collections",
        "abc",
    } or node.module.startswith("pypp_python"):
        return
    module_str = node.module.replace(".", "/") + ".h"
    for alias in node.names:
        assert alias.asname is None, "'as' is not supported in import from"
        imp_map[alias.name] = QInc(module_str)
