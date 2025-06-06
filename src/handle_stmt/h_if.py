import ast

from src.d_types import CppInclude


def handle_if(
    node: ast.If,
    ret_imports: set[CppInclude],
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    test_str = handle_expr(node.test, ret_imports)
    # TODO: probably extract a helper function for this iterations
    body: list[str] = []
    for body_node in node.body:
        body.append(handle_stmt(body_node, ret_imports, ret_h_file))
    body_str = "".join(body)
    or_else: list[str] = []
    for or_else_node in node.orelse:
        or_else.append(handle_stmt(or_else_node, ret_imports, ret_h_file))
    if len(or_else) == 0:
        return f"if ({test_str}) {{{body_str}}}"
    or_else_str = "".join(or_else)
    return f"if ({test_str}) {{{body_str}}} else {{{or_else_str}}}"
