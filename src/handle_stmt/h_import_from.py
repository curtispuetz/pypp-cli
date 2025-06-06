import ast

from src.d_types import CppInclude, QInc


def handle_import_from(node: ast.ImportFrom, ret_imports: set[CppInclude]) -> str:
    assert node.module is not None, "Not supported"
    assert node.level == 0, "Only absolute import supported"
    # NOTE: do not name any other directories .src
    module_str = node.module.replace(".", "/") + ".h"
    ret_imports.add(QInc(module_str))
    return ""
