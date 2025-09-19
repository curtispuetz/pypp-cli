import ast

from pypp_cli.do.y.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.y.d_types import AngInc
from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from pypp_cli.do.transpile.transpile.calc_code.z.handlers.mapping.exceptions import (
    lookup_cpp_exception_type,
)


from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExceptionHandlersHandler:
    _d: Deps

    def handle(self, nodes: list[ast.ExceptHandler]) -> str:
        return " ".join(self._handle_exception_handler(node) for node in nodes)

    def _handle_exception_handler(self, node: ast.ExceptHandler) -> str:
        body_str = self._d.handle_stmts(node.body)
        exc_str: str
        if node.type is not None:
            if not isinstance(node.type, ast.Name):
                self._d.value_err(
                    "Can only catch one exception type at a time", node.type
                )
            name_str = self._d.handle_expr(node.type)
            exc_str = f"const {lookup_cpp_exception_type(name_str, self._d)}&"
            if node.name is not None:
                assert isinstance(node.name, str), SHOULDNT_HAPPEN
                exc_str += f" pypp_pseudo_name_{node.name}"
                self._d.add_inc(AngInc("string"))
                body_str = (
                    f"std::string {node.name} = pypp_pseudo_name_{node.name}.msg_; "
                    + body_str
                )
        else:
            exc_str = "..."
        return f"catch ({exc_str})" + "{" + body_str + "}"
