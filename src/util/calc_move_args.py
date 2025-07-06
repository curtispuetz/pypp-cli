import ast

from src.util.ret_imports import RetImports


def calc_move_args(
    args: list[ast.expr],
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
) -> str:
    ret: list[str] = []
    for arg in args:
        x = handle_expr(arg, ret_imports, include_in_header)
        if isinstance(arg, ast.Name):
            # TODO later: Confirm that ast.Name is the only case where we need to move
            x = "std::move(" + x + ")"
        ret.append(x)
    return ", ".join(ret)
