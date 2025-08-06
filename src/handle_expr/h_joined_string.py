import ast

from src.d_types import QInc
from src.deps import Deps
from src.util.ret_imports import add_inc


def handle_joined_string(
    node: ast.JoinedStr,
    d: Deps,
    include_in_header: bool,
) -> str:
    add_inc(d.ret_imports, QInc("py_str.h"), include_in_header)
    std_format_args: list[str] = []
    std_format_first_arg: list[str] = []
    for n in node.values:
        if isinstance(n, ast.Constant):
            assert isinstance(n.value, str), "Shouldn't happen"
            std_format_first_arg.append(n.value)
        else:
            assert isinstance(n, ast.FormattedValue), "Shouldn't happen"
            std_format_first_arg.append("{}")
            std_format_args.append(handle_formatted_value(n, d, include_in_header))
    first_arg_str: str = "".join(std_format_first_arg)
    args_str: str = ", ".join(std_format_args)
    return f'PyStr(std::format("{first_arg_str}", {args_str}))'


def handle_formatted_value(
    node: ast.FormattedValue,
    d: Deps,
    include_in_header: bool,
) -> str:
    assert node.conversion == -1, "formatting with f strings not supported"
    assert node.format_spec is None, "Nested f-stream feature not supported"
    return d.handle_expr(node.value, include_in_header)
