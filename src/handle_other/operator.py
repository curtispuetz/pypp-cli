# ast docs: operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
#                  | RShift | BitOr | BitXor | BitAnd | FloorDiv
import ast

from src.d_types import CppInclude, QInc


def handle_operator(
    node: ast.operator, ret_imports: set[CppInclude]
) -> tuple[str, str, str]:
    if isinstance(node, ast.Add):
        return "", "+", ""
    if isinstance(node, ast.Sub):
        return "", "-", ""
    if isinstance(node, ast.Mult):
        return "", "*", ""
    if isinstance(node, ast.Div):
        return "", "/", ""
    if isinstance(node, ast.FloorDiv):
        ret_imports.add(QInc("pypp_util/floor_div.h"))
        return "py_floor_div(", ", ", ")"
    raise Exception(f"operator type {node} is not handled")


def handle_operator_for_aug_assign(node: ast.operator) -> str:
    assert not isinstance(node, ast.FloorDiv), "shouldn't happen"
    return handle_operator(node, set())[1]
