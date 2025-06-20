import ast
from dataclasses import dataclass

from src.d_types import QInc
from src.util.handle_lists import handle_stmts
from src.util.inner_strings import calc_inside_rd
from src.util.ret_imports import RetImports, add_inc


# TODO: handle enumerate(), zip(), and reverse() keywords
def handle_for(
    node: ast.For,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    assert len(node.orelse) == 0, "For loop else not supported"
    assert node.type_comment is None, "For loop type comment not supported"
    body_str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    target_str: str = handle_expr(node.target, ret_imports)
    iter_str = handle_expr(node.iter, ret_imports)
    if iter_str.startswith("PyEnumerate(") and iter_str.endswith(")"):
        add_inc(ret_imports, QInc("py_enumerate.h"))
    elif iter_str.startswith("PyZip(") and iter_str.endswith(")"):
        add_inc(ret_imports, QInc("py_zip.h"))
    elif iter_str.startswith("PyRange(") and iter_str.endswith(")"):
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
    if target_str.startswith("PyTup(") and target_str.endswith(")"):
        inner_args = calc_inside_rd(target_str).split(", ")
        target_str = "pypp_hardcoded_it_tup"  # hardcoded value that should not be used
        add_to_body_str: list[str] = []
        for i, inner_arg in enumerate(inner_args):
            add_to_body_str.append(f"auto &{inner_arg} = {target_str}.get<{i}>();")
        body_str = "".join(add_to_body_str) + body_str
    return f"for (const auto &{target_str} : {iter_str})" + "{" + body_str + "}"


@dataclass(frozen=True, slots=True)
class _IterArgs:
    start: int
    stop: int
    step: int


def _calc_iter_args(s: str) -> _IterArgs:
    arr: list[str] = s.split("(", 1)[1][:-1].split(",")
    if len(arr) == 3:
        return _IterArgs(*(int(a) for a in arr))
    if len(arr) == 2:
        # start and stop were supplied
        return _IterArgs(int(arr[0]), int(arr[1]), 1)
    if len(arr) == 1:
        # stop was supplied
        return _IterArgs(0, int(arr[0]), 1)
    raise AssertionError("Shouldn't happen")
