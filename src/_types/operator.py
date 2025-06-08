# ast docs: operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
#                  | RShift | BitOr | BitXor | BitAnd | FloorDiv
import ast

from src.d_types import CppInclude, QInc


def lookup_op(_type: ast.operator, ret_imports: set[CppInclude]) -> tuple[str, str, str]:
    if isinstance(_type, ast.Add):
        return "", "+", ""
    if isinstance(_type, ast.Sub):
        return "", "-", ""
    if isinstance(_type, ast.Mult):
        return "", "*", ""
    if isinstance(_type, ast.Div):
        return "", "/", ""
    if isinstance(_type, ast.FloorDiv):
        ret_imports.add(QInc("pypp_util/floor_div.h"))
        return "py_floor_div(", ", ", ")"
    raise f"cmpop type {_type} is not handled"
