import ast
from dataclasses import dataclass

from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_tuple import handle_tuple_inner_args


def handle_for(node: ast.For, d: Deps) -> str:
    assert len(node.orelse) == 0, "For loop else not supported"
    assert node.type_comment is None, "For loop type comment not supported"
    body_str = d.handle_stmts(node.body)
    if isinstance(node.target, ast.Tuple):
        target_str = "[" + handle_tuple_inner_args(node.target, d) + "]"
    else:
        target_str: str = d.handle_expr(node.target)
    iter_str = d.handle_expr(node.iter)
    if iter_str.startswith("PyRange(") and iter_str.endswith(")"):
        # This is not necessary because PyRange can be iterated over directly, but if
        # it is used explicitly in the loop, I might as well convert it to the
        # traditional C++ for loop syntax, since it is slightly more performant.
        iter_args: _IterArgs = _calc_iter_args(iter_str)
        return (
            f"for (int {target_str} = {iter_args.start}; {target_str} < {iter_args.stop}; {target_str} += {iter_args.step}) "
            + "{"
            + body_str
            + "}"
        )
    # Note: I use const here because in Py++ I am thinking targets of range-based for
    #  loops should not be modified.
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
    raise AssertionError("Shouldn't happen")
