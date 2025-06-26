import ast

from src.handle_stmt.h_for import handle_for
from src.util.ret_imports import RetImports


def handle_list_comp(
    node: ast.ListComp,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
    handle_stmt,
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
    append_call_node: ast.Call = ast.Call(
        func=ast.Attribute(
            value=ast.Name(id=target_str, ctx=ast.Load()),
            attr="append",
            ctx=ast.Load(),
        ),
        args=[node.elt],
        keywords=[],
    )
    append_exp_node: ast.Expr = ast.Expr(value=append_call_node)
    for_node: ast.For = ast.For(
        target=gen_node.target,
        iter=gen_node.iter,
        body=[append_exp_node],
        orelse=[],
        type_comment=None,
    )
    return handle_for(for_node, ret_imports, ret_h_file, handle_stmt, handle_expr)
