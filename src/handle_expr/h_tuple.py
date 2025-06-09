import ast

from src.d_types import CppInclude
from src.util.handle_lists import handle_exprs


def handle_tuple(node: ast.Tuple, ret_imports: set[CppInclude], handle_expr) -> str:
    return handle_exprs(node.elts, ret_imports, handle_expr)
