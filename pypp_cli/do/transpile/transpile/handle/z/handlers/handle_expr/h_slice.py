import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.z.d_types import QInc
from pypp_cli.do.transpile.transpile.handle.node import Deps


@dataclass(frozen=True, slots=True)
class SliceHandler:
    _d: Deps

    def handle(self, node: ast.Slice) -> str:
        # NOTE: The C++ code handles Nones for start, but this code just wont use that.
        # Which is maybe fine
        self._d.add_inc(QInc("slice/creators.h"))
        lower: str = "0" if node.lower is None else self._d.handle_expr(node.lower)
        step: str = "1" if node.step is None else self._d.handle_expr(node.step)
        upper: str = (
            "std::nullopt" if node.upper is None else self._d.handle_expr(node.upper)
        )
        return f"pypp::py_slice({lower}, {upper}, {step})"
