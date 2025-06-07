import ast

from src.d_types import CppInclude


def handle_if(
    node: ast.If,
    ret_imports: set[CppInclude],
    ret_h_file: list[str],
    handle_stmt,
    handle_stmts,
    handle_expr,
) -> str:
    test_str = handle_expr(node.test, ret_imports)
    body_str = handle_stmts(node.body, ret_imports, ret_h_file)
    if len(node.orelse) == 0:
        return "if (" + test_str + ") {" + body_str + "}"
    if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
        return _if_else_body(test_str, body_str) + handle_if(
            node.orelse[0],
            ret_imports,
            ret_h_file,
            handle_stmt,
            handle_stmts,
            handle_expr,
        )
    else:
        or_else: list[str] = []
        for or_else_node in node.orelse:
            or_else.append(handle_stmt(or_else_node, ret_imports, ret_h_file))
        or_else_str = "".join(or_else)

        return f"{_if_else_body(test_str, body_str)}{{{or_else_str}}}"


def _if_else_body(test_str: str, body_str: str) -> str:
    return "if (" + test_str + ") {" + body_str + "} else "

