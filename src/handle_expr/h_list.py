import ast

from src.d_types import QInc
from src.deps import Deps
from src.util.calc_move_args import calc_move_args

# TODO later: I need like a 'list_reserve' function that can be used to reserve space
#  in the underlying C++ std::vector. This lets Py++ users improve performance.


# Note: inline list creation is a little inefficient just because initializer lists in
# C++ are a little inefficient. For small data though, they are fine.
def handle_list(
    node: ast.List,
    d: Deps,
    include_in_header: bool,
) -> str:
    d.add_inc(QInc("py_list.h"), include_in_header)
    args_str: str = calc_move_args(node.elts, d, include_in_header)
    return "PyList({" + args_str + "})"
