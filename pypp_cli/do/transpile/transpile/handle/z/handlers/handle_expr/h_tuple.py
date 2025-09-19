import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.z.d_types import QInc
from pypp_cli.do.transpile.transpile.handle.node import Deps


def handle_tuple_inner_args(node: ast.Tuple, d: Deps):
    return d.handle_exprs(node.elts)


@dataclass(frozen=True, slots=True)
class TupleHandler:
    _d: Deps

    def handle(self, node: ast.Tuple) -> str:
        self._d.add_inc(QInc("py_tuple.h"))
        args_str: str = self._d.handle_exprs(node.elts)
        return f"pypp::PyTup({args_str})"
