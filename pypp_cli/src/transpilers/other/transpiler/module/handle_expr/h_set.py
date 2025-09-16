import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps


@dataclass(frozen=True, slots=True)
class SetHandler:
    _d: Deps

    def handle(self, node: ast.Set) -> str:
        self._d.add_inc(QInc("py_set.h"))
        return "pypp::PySet({" + self._d.handle_exprs(node.elts) + "})"
