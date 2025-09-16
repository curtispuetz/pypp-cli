import ast
from dataclasses import dataclass

from pypp_cli.src.config import SHOULDNT_HAPPEN
from pypp_cli.src.transpilers.other.transpiler.d_types import QInc, AngInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps


# ast docs: operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
#                  | RShift | BitOr | BitXor | BitAnd | FloorDiv


@dataclass(frozen=True, slots=True)
class OperatorHandler:
    _d: Deps

    def handle(self, node: ast.operator) -> tuple[str, str, str]:
        res = self._handle_operator(node)
        if res is not None:
            return res
        if isinstance(node, ast.Pow):
            self._d.add_inc(AngInc("cmath"))
            return "std::pow(", ", ", ")"
        if isinstance(node, ast.FloorDiv):
            self._d.add_inc(QInc("pypp_util/floor_div.h"))
            return "pypp::py_floor_div(", ", ", ")"
        raise ValueError(f"operator type {node} is not supported")

    def handle_for_aug_assign(self, node: ast.operator) -> str:
        if isinstance(node, ast.FloorDiv):
            self._d.value_err_no_ast("//= not supported")
        if isinstance(node, ast.Pow):
            self._d.value_err_no_ast("**= not supported")
        res = self._handle_operator(node)
        assert res is not None, SHOULDNT_HAPPEN
        return res[1]

    def _handle_operator(self, node: ast.operator) -> tuple[str, str, str] | None:
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
            self._d.value_err_no_ast("Matrix mult operator (i.e. @) not supported")
        return None
