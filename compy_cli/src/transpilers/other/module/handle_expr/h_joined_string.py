import ast

from compy_cli.src.transpilers.other.module.d_types import QInc
from compy_cli.src.transpilers.other.module.deps import Deps


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
    first_arg_str: str = "".join(std_format_first_arg)
    args_str: str = ", ".join(std_format_args)
    return f'PyStr(std::format("{first_arg_str}", {args_str}))'


def handle_formatted_value(node: ast.FormattedValue, d: Deps) -> str:
    assert node.conversion == -1, "formatting with f strings not supported"
    assert node.format_spec is None, "Nested f-stream feature not supported"
    return d.handle_expr(node.value)
