import ast
from typing import cast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_for import (
    handle_for,
)


def handle_comp(
    node: ast.ListComp | ast.SetComp | ast.DictComp,
    d: Deps,
    target_str: str,
) -> str:
    # It should be converted to a for loop.
    # The list comprehension must be assigned to something.
    assert len(node.generators) == 1, (
        "multiple loops not supported in list comprehensions"
    )
    gen_node = node.generators[0]
    assert len(gen_node.ifs) == 0, "ifs not supported in list comprehensions"
    assert not gen_node.is_async, "async not supported in list comprehensions"
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
    return handle_for(for_node, d)
