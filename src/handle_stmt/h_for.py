import ast
from dataclasses import dataclass

from src.d_types import CppInclude
from src.util.handle_lists import handle_stmts


def handle_for(
    node: ast.For,
    ret_imports: set[CppInclude],
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    assert len(node.orelse) == 0, "For loop else not supported"
    assert node.type_comment is None, "For loop type comment not supported"
    body_str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    target_str = handle_expr(node.target, ret_imports)
    iter_str = handle_expr(node.iter, ret_imports)
    if iter_str.startswith("range(") and iter_str.endswith(")"):
        iter_args: _IterArgs = _calc_iter_args(iter_str)
        return (
            f"for (int {target_str} = {iter_args.start}; i < {iter_args.stop}; i += {iter_args.step}) "
            + "{"
            + body_str
            + "}"
        )
    return f"for (auto {target_str} : {iter_str})" + "{" + body_str + "}"


@dataclass(frozen=True, slots=True)
class _IterArgs:
    start: int
    stop: int
    step: int


def _calc_iter_args(s: str) -> _IterArgs:
    arr: list[str] = s.split("(", 1)[1][:-1].split(",")
    return _IterArgs(*(int(a) for a in arr))
