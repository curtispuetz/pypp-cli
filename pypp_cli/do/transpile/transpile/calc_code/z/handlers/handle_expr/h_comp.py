import ast
from dataclasses import dataclass
from typing import cast

from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from pypp_cli.do.transpile.transpile.calc_code.z.handlers.handle_stmt.h_for import (
    ForHandler,
)


@dataclass(frozen=True, slots=True)
class CompHandler:
    _d: Deps
    _for_handler: ForHandler

    def handle(
        self,
        node: ast.ListComp | ast.SetComp | ast.DictComp,
        target_str: str,
    ) -> str:
        # It should be converted to a for loop.
        # The list comprehension must be assigned to something.
        if len(node.generators) != 1:
            self._d.value_err(
                "multiple loops not supported in list comprehensions", node
            )
        gen_node = node.generators[0]
        if len(gen_node.ifs) != 0:
            self._d.value_err("ifs not supported in list comprehensions", node)
        if gen_node.is_async:
            self._d.value_err("async not supported in list comprehensions", node)
        logic_exp_node: ast.stmt
        if isinstance(node, ast.DictComp):
            # a[3] = "d"
            logic_exp_node = ast.Assign(
                targets=[
                    ast.Subscript(
                        value=ast.Name(id=target_str, ctx=ast.Load()),
                        slice=node.key,
                        ctx=ast.Store(),
                    )
                ],
                value=node.value,
                type_comment=None,
            )
        else:
            append_or_add_node: ast.Call = ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id=target_str, ctx=ast.Load()),
                    attr="append" if isinstance(node, ast.ListComp) else "add",
                    ctx=ast.Load(),
                ),
                args=[node.elt],
                keywords=[],
            )
            logic_exp_node = ast.Expr(value=cast(ast.expr, append_or_add_node))
        for_node: ast.For = ast.For(
            target=gen_node.target,
            iter=gen_node.iter,
            body=[logic_exp_node],
            orelse=[],
            type_comment=None,
        )
        return self._for_handler.handle(for_node)
