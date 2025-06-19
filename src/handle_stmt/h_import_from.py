import ast

from src.d_types import QInc
from src.util.ret_imports import ImpMap


# TODO Note: I could make a map here of names to QInc required
#  and then pass that map everywhere and decide whether to put it in the header
#  or cpp files based on where the name is used. That would also require
#  processing these import statements separately at the beginning, and not allowing
#  import statements anywhere but at the top of the file before everything else.
def handle_import_from(node: ast.ImportFrom, imp_map: ImpMap):
    assert node.module is not None, "Not supported"
    assert node.level == 0, "Only absolute import supported"
    # NOTE: do not name any other directories .src
    module_str = node.module.replace(".", "/") + ".h"
    for alias in node.names:
        imp_map[alias.name] = QInc(module_str)
    return ""
