import ast

from compy_cli.src.d_types import QInc
from compy_cli.src.deps import Deps


# Note: inline list creation is a little inefficient just because initializer lists in
# C++ are a little inefficient. For small data though, they are fine.
def handle_list(node: ast.List, d: Deps) -> str:
    d.add_inc(QInc("py_list.h"))
    args_str: str = d.handle_exprs(node.elts)
    return "PyList({" + args_str + "})"
