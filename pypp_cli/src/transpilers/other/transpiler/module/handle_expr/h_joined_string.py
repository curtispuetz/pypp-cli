import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_constant import (
    SPECIAL_CHAR_MAP,
)


def handle_joined_string(node: ast.JoinedStr, d: Deps) -> str:
    d.add_inc(QInc("py_str.h"))
    std_format_args: list[str] = []
    std_format_first_arg: list[str] = []
    for n in node.values:
        if isinstance(n, ast.Constant):
            assert isinstance(n.value, str), "Shouldn't happen"
            std_format_first_arg.append(n.value)
        else:
            assert isinstance(n, ast.FormattedValue), "Shouldn't happen"
            std_format_first_arg.append("{}")
            std_format_args.append(handle_formatted_value(n, d))
    first_arg_str: str = "".join(std_format_first_arg).translate(SPECIAL_CHAR_MAP)
    args_str: str = ", ".join(std_format_args)
    return f'pypp::PyStr(std::format("{first_arg_str}", {args_str}))'


def handle_formatted_value(node: ast.FormattedValue, d: Deps) -> str:
    if node.conversion != -1:
        d.value_err(
            "f-string conversion flags (i.e. '!r', '!a', '!s') are not supported", node
        )
    if node.format_spec is not None:
        d.value_err(
            "Format specifications in f-strings (e.g. ':.2f', etc.) not supported", node
        )
    return d.handle_expr(node.value)
