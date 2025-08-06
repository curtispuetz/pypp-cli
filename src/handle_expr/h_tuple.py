import ast

from src.d_types import QInc
from src.deps import Deps
from src.util.calc_move_args import calc_move_args
from src.util.handle_lists import handle_exprs
from src.util.ret_imports import add_inc


def handle_tuple_inner_args(
    node: ast.Tuple,
    d: Deps,
    include_in_header: bool = False,
):
    return handle_exprs(node.elts, d, include_in_header)


def handle_tuple(
    node: ast.Tuple,
    d: Deps,
    include_in_header: bool,
) -> str:
    # TODO: remove first argument
    add_inc(d.ret_imports, QInc("py_tuple.h"), include_in_header)
    args_str: str = calc_move_args(node.elts, d, include_in_header)
    return f"PyTup({args_str})"
