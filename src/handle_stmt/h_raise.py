import ast

from src.d_types import CppInclude
from src.mapping.exceptions import lookup_cpp_exception_type
from src.util.inner_strings import calc_inside_rd


def handle_raise(node: ast.Raise, ret_imports: set[CppInclude], handle_expr) -> str:
    assert node.cause is None, "exception cause not supported"
    assert node.exc is not None, "raising without exception type is not supported"
    exe_str = handle_expr(node.exc, ret_imports)
    inside_str = calc_inside_rd(exe_str)
    python_exception_type = exe_str.split("(", 1)[0]
    cpp_exception_type = lookup_cpp_exception_type(python_exception_type, ret_imports)
    # NOTE: assuming here that the inside part is always a PyStr with the str() method.
    #  I think this is true?
    return f"throw {cpp_exception_type}({inside_str}.str());"
