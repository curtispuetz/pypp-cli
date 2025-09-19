import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.transpile.z.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.transpile.z.d_types import QInc
from pypp_cli.do.transpile.transpile.transpile.node import Deps
from pypp_cli.do.transpile.transpile.transpile.z.handlers.handle_expr.h_tuple import (
    handle_tuple_inner_args,
)


@dataclass(frozen=True, slots=True)
class ForHandler:
    _d: Deps

    def handle(self, node: ast.For) -> str:
        if len(node.orelse) != 0:
            self._d.value_err_no_ast("For loop else not supported")
        if node.type_comment is not None:
            self._d.value_err_no_ast("For loop type comment not supported")
        body_str = self._d.handle_stmts(node.body)
        if isinstance(node.target, ast.Tuple):
            target_str = "[" + handle_tuple_inner_args(node.target, self._d) + "]"
        else:
            target_str: str = self._d.handle_expr(node.target)
        range_inc = QInc("py_range.h")
        has_range_include = self._d.cpp_includes.contains(range_inc)
        iter_str = self._d.handle_expr(node.iter)
        if iter_str.startswith("pypp::PyRange(") and iter_str.endswith(")"):
            if not has_range_include:
                self._d.cpp_includes.discard(range_inc)
            # This is not necessary because PyRange can be iterated over directly, but
            # if it is used explicitly in the loop, I might as well convert it to the
            # traditional C++ for loop syntax, since it is slightly more performant.
            iter_args: _IterArgs = _calc_iter_args(iter_str)
            return (
                f"for (int {target_str} = {iter_args.start}; "
                f"{target_str} < {iter_args.stop}; {target_str} += {iter_args.step}) "
                + "{"
                + body_str
                + "}"
            )
        # Note: I use const here because in Py++ I am thinking targets of range-based
        # for loops should not be modified. In the future we can maybe change that. But
        # for now I want to keep it safe that users do not reassign the variable, since
        # that behavior works different in C++ vs. Python.
        return f"for (const auto &{target_str} : {iter_str})" + "{" + body_str + "}"


@dataclass(frozen=True, slots=True)
class _IterArgs:
    start: int | str
    stop: int | str
    step: int | str


def _calc_iter_args(s: str) -> _IterArgs:
    arr: list[str] = s.split("(", 1)[1][:-1].split(",")
    if len(arr) == 3:
        return _IterArgs(*(a for a in arr))
    if len(arr) == 2:
        # start and stop were supplied
        return _IterArgs(arr[0], arr[1], 1)
    if len(arr) == 1:
        # stop was supplied
        return _IterArgs(0, arr[0], 1)
    raise AssertionError(SHOULDNT_HAPPEN)
