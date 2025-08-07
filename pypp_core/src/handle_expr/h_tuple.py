import ast

from pypp_core.src.d_types import QInc
from pypp_core.src.deps import Deps
from pypp_core.src.util.calc_move_args import calc_move_args
from pypp_core.src.util.handle_lists import handle_exprs


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
    d.add_inc(QInc("py_tuple.h"), include_in_header)
    args_str: str = calc_move_args(node.elts, d, include_in_header)
    return f"PyTup({args_str})"
