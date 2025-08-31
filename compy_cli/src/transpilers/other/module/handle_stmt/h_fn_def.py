import ast

from compy_cli.src.transpilers.other.module.deps import Deps
from compy_cli.src.transpilers.other.module.util.calc_fn_signature import (
    calc_fn_signature,
    calc_fn_str_with_body,
)


# TODO later: consider naming collisions in general in the C++ transpiled code. What
#  easy strategies can I do to prevent them?


def handle_fn_def(node: ast.FunctionDef, d: Deps) -> str:
    assert len(node.decorator_list) == 0, "function decorators are not supported"
    fn_name = node.name
    fn_name_doesnt_start_with_underscore: bool = not fn_name.startswith("_")
    d.set_inc_in_h(fn_name_doesnt_start_with_underscore)
    fn_signature = calc_fn_signature(node, d, fn_name)
    d.set_inc_in_h(False)
    if fn_name_doesnt_start_with_underscore:
        d.ret_h_file.append(fn_signature + ";")
    body_str: str = d.handle_stmts(node.body)
    return calc_fn_str_with_body(fn_signature, body_str)
