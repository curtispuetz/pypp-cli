import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.z.d_types import QInc
from pypp_cli.do.transpile.transpile.handle.node import Deps


_ERR_STR: str = (
    "With statement can only be used as 'with open(arg1, optional_arg2) as name1'"
)


@dataclass(frozen=True, slots=True)
class WithItemHandler:
    _d: Deps

    def handle(self, nodes: list[ast.withitem]) -> str:
        node, args = self._assert_with_item_is_open(nodes)
        args_str = self._d.handle_exprs(args)
        variable_name = self._get_var_name(node)
        self._d.add_inc(QInc("pypp_text_io.h"))
        return f"pypp::PyTextIO {variable_name}({args_str});"

    def _assert_with_item_is_open(
        self, nodes: list[ast.withitem]
    ) -> tuple[ast.withitem, list[ast.expr]]:
        if len(nodes) != 1:
            self._d.value_err_no_ast(_ERR_STR)
        node = nodes[0]
        if not isinstance(node.context_expr, ast.Call):
            self._d.value_err(_ERR_STR, node)
        elif not isinstance(node.context_expr.func, ast.Name):
            self._d.value_err(_ERR_STR, node)
        elif not node.context_expr.func.id == "open":
            self._d.value_err(_ERR_STR, node)
        elif len(node.context_expr.args) not in {1, 2}:
            self._d.value_err("open() expected 1 or 2 arguments", node)
        return node, node.context_expr.args

    def _get_var_name(self, node: ast.withitem) -> str:
        if node.optional_vars is None:
            self._d.value_err(_ERR_STR, node)
        elif not isinstance(node.optional_vars, ast.Name):
            self._d.value_err(_ERR_STR, node)
        elif not isinstance(node.optional_vars.id, str):
            self._d.value_err(_ERR_STR, node)
        return node.optional_vars.id
