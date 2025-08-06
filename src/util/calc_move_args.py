import ast

from src.deps import Deps


def calc_move_args(
    args: list[ast.expr],
    d: Deps,
    include_in_header: bool,
) -> str:
    ret: list[str] = []
    for arg in args:
        x = d.handle_expr(arg, include_in_header)
        if isinstance(arg, ast.Name):
            # TODO later: Confirm that ast.Name is the only case where we need to move
            x = "std::move(" + x + ")"
        ret.append(x)
    return ", ".join(ret)
