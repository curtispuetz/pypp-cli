import ast

from src.util.calc_fn_signature import calc_fn_signature, calc_fn_str_with_body
from src.util.handle_lists import handle_stmts
from src.util.ret_imports import RetImports


# TODO later: consider naming collisions in general in the C++ transpiled code. What
#  easy strategies can I do to prevent them?


def handle_fn_def(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    assert len(node.decorator_list) == 0, "function decorators are not supported"
    fn_name = node.name
    fn_name_doesnt_start_with_underscore: bool = not fn_name.startswith("_")
    fn_signature = calc_fn_signature(
        node, ret_imports, handle_expr, fn_name, fn_name_doesnt_start_with_underscore
    )
    if fn_name_doesnt_start_with_underscore:
        ret_h_file.append(fn_signature + ";")
    body_str: str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    return calc_fn_str_with_body(fn_signature, body_str)
