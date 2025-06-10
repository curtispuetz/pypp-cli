import ast

from src.d_types import CppInclude, QInc
from src.util.handle_lists import handle_exprs


def handle_set(node: ast.Set, ret_imports: set[CppInclude], handle_expr) -> str:
    ret_imports.add(QInc("py_set.h"))
    return "PySet({" + handle_exprs(node.elts, ret_imports, handle_expr) + "})"
