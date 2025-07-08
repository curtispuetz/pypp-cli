# ast docs: operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
#                  | RShift | BitOr | BitXor | BitAnd | FloorDiv
import ast

from src.d_types import QInc, AngInc
from src.util.ret_imports import RetImports, add_inc


# TODO: handle more. Especially Pow and Mod.
def handle_operator(
    node: ast.operator, ret_imports: RetImports | None
) -> tuple[str, str, str]:
    if isinstance(node, ast.Add):
        return "", "+", ""
    if isinstance(node, ast.Sub):
        return "", "-", ""
    if isinstance(node, ast.Mult):
        return "", "*", ""
    if isinstance(node, ast.Div):
        return "", "/", ""
    if isinstance(node, ast.Mod):
        return "", "%", ""
    if isinstance(node, ast.LShift):
        return "", "<<", ""
    if isinstance(node, ast.RShift):
        return "", ">>", ""
    if isinstance(node, ast.BitOr):
        return "", "|", ""
    if isinstance(node, ast.BitXor):
        return "", "^", ""
    if isinstance(node, ast.BitAnd):
        return "", "&", ""
    if isinstance(node, ast.Pow):
        add_inc(ret_imports, AngInc("cmath"))
        return "std::pow(", ", ", ")"
    if isinstance(node, ast.FloorDiv):
        add_inc(ret_imports, QInc("pypp_util/floor_div.h"))
        return "py_floor_div(", ", ", ")"
    # Note:
    # - MatMult is not supported because its mostly just used for numpy arrays.
    raise Exception(f"operator type {node} is not handled")


def handle_operator_for_aug_assign(node: ast.operator) -> str:
    assert not isinstance(node, ast.FloorDiv), "shouldn't happen"
    return handle_operator(node, None)[1]
