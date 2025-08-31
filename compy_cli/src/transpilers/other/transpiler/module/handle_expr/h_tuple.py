import ast

from compy_cli.src.transpilers.other.transpiler.d_types import QInc
from compy_cli.src.transpilers.other.transpiler.deps import Deps


def handle_tuple_inner_args(node: ast.Tuple, d: Deps):
    return d.handle_exprs(node.elts)


def handle_tuple(node: ast.Tuple, d: Deps) -> str:
    d.add_inc(QInc("py_tuple.h"))
    args_str: str = d.handle_exprs(node.elts)
    return f"PyTup({args_str})"
