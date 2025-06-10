import ast

from src.d_types import CppInclude
from src.util.handle_lists import handle_exprs


def handle_tuple(node: ast.Tuple, ret_imports: set[CppInclude], handle_expr) -> str:
    # Note for later: The node.ctx will tell you if you are loading values
    #  like a, b, c = my_fn(). So I can use it for that.
    return "PyTup(" + handle_exprs(node.elts, ret_imports, handle_expr) + ")"
