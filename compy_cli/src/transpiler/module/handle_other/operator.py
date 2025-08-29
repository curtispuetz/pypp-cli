# ast docs: operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
#                  | RShift | BitOr | BitXor | BitAnd | FloorDiv
import ast

from compy_cli.src.transpiler.module.d_types import QInc, AngInc
from compy_cli.src.transpiler.module.deps import Deps


def _handle_operator(node: ast.operator) -> tuple[str, str, str] | None:
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
    if isinstance(node, ast.MatMult):
        # MatMult is not supported because its mostly just used for numpy arrays.
        raise ValueError("Matrix mult operator (i.e. @) not supported")
    return None


def handle_operator(node: ast.operator, d: Deps) -> tuple[str, str, str]:
    res = _handle_operator(node)
    if res is not None:
        return res
    if isinstance(node, ast.Pow):
        d.add_inc(AngInc("cmath"))
        return "std::pow(", ", ", ")"
    if isinstance(node, ast.FloorDiv):
        d.add_inc(QInc("compy_util/floor_div.h"))
        return "py_floor_div(", ", ", ")"
    raise Exception(f"operator type {node} is not handled")


def handle_operator_for_aug_assign(node: ast.operator) -> str:
    assert not isinstance(node, ast.FloorDiv), "//= not supported"
    assert not isinstance(node, ast.Pow), "**= not supported"
    res = _handle_operator(node)
    assert res is not None, "shouldn't happen"
    return res[1]
