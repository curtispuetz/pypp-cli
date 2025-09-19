import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.z_i.d_types import QInc
from pypp_cli.do.transpile.transpile.handle.node import Deps


@dataclass(frozen=True, slots=True)
class SetHandler:
    _d: Deps

    def handle(self, node: ast.Set) -> str:
        self._d.add_inc(QInc("py_set.h"))
        return "pypp::PySet({" + self._d.handle_exprs(node.elts) + "})"
