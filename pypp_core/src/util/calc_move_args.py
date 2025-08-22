import ast

from pypp_core.src.deps import Deps


def calc_move_args(args: list[ast.expr], d: Deps) -> str:
    # TODO: I think delete this because users have to use mov() if thats what they want
    #  Is it the case that a list and tuple and dict don't accept lvalue references?
    ret: list[str] = []
    for arg in args:
        x = d.handle_expr(arg)
        if isinstance(arg, ast.Name):
            # TODO later: Confirm that ast.Name is the only case where we need to move
            x = "std::move(" + x + ")"
        ret.append(x)
    return ", ".join(ret)
