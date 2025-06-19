import ast

from src.d_types import CppInclude, QInc


def handle_joined_string(
    node: ast.JoinedStr, ret_imports: set[CppInclude], handle_expr
) -> str:
    ret_imports.add(QInc("py_str.h"))
    std_format_args: list[str] = []
    std_format_first_arg: list[str] = []
    for n in node.values:
        if isinstance(n, ast.Constant):
            assert isinstance(n.value, str), "Shouldn't happen"
            std_format_first_arg.append(n.value)
        else:
            assert isinstance(n, ast.FormattedValue), "Shouldn't happen"
            std_format_first_arg.append("{}")
            std_format_args.append(handle_formatted_value(n, ret_imports, handle_expr))
    first_arg_str: str = "".join(std_format_first_arg)
    args_str: str = ", ".join(std_format_args)
    return f'PyStr(std::format("{first_arg_str}", {args_str}))'


def handle_formatted_value(
    node: ast.FormattedValue, ret_imports: set[CppInclude], handle_expr
) -> str:
    assert node.conversion == -1, "formatting with f strings not supported"
    # shouldn't happen if node.conversion is -1
    assert node.format_spec is None, "Shouldn't happen"
    return handle_expr(node.value, ret_imports)
