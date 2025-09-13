import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.util.calc_fn_signature import (
    calc_fn_signature,
    calc_fn_str_with_body,
)


# Underscore rules:
# - If the function starts with an underscore, then; 1) it is not defined in the header
# file and 2) it gets a `static` prefix so that name conflicts can be avoided.


def handle_fn_def(node: ast.FunctionDef, d: Deps) -> str:
    if len(node.decorator_list) != 0:
        d.value_err_no_ast(
            f"function decorators are not supported. Problem function: {node.name}"
        )
    fn_name = node.name
    is_header_defined: bool = not fn_name.startswith("_")

    d.set_inc_in_h(is_header_defined)
    fn_signature: str = calc_fn_signature(node, d, fn_name)
    d.set_inc_in_h(False)

    if is_header_defined:
        d.ret_h_file.append(fn_signature + ";")
    else:
        fn_signature = "static " + fn_signature
    body_str: str = d.handle_stmts(node.body)
    return calc_fn_str_with_body(fn_signature, body_str)
