import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.z_i.d_types import QInc
from pypp_cli.do.transpile.transpile.handle.z.deps import Deps


@dataclass(frozen=True, slots=True)
class ListHandler:
    _d: Deps

    def handle(self, node: ast.List) -> str:
        # Note: inline list creation is a little inefficient just because initializer
        # lists in C++ are a little inefficient. For small data though, they are fine.
        self._d.add_inc(QInc("py_list.h"))
        args_str: str = self._d.handle_exprs(node.elts)
        return "pypp::PyList({" + args_str + "})"
