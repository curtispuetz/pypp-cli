import ast

from pypp_core.src.d_types import QInc
from pypp_core.src.deps import Deps

# TODO later: I need like a 'list_reserve' function that can be used to reserve space
#  in the underlying C++ std::vector. This lets Py++ users improve performance.


# Note: inline list creation is a little inefficient just because initializer lists in
# C++ are a little inefficient. For small data though, they are fine.
def handle_list(node: ast.List, d: Deps) -> str:
    d.add_inc(QInc("py_list.h"))
    args_str: str = d.handle_exprs(node.elts)
    return "PyList({" + args_str + "})"
