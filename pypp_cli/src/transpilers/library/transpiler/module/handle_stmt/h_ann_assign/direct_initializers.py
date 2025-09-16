import ast

from pypp_cli.src.transpilers.library.transpiler.module.util.inner_strings import (
    calc_inside_rd,
)


_DIRECT_INITIALIZERS: dict[str, type] = {
    "pypp::PyList": ast.List,
    "pypp::PySet": ast.Set,
}


def calc_value_str_for_direct_init(node: ast.AnnAssign, value_str: str) -> str | None:
    i: int = value_str.find("(")
    if i != -1:
        func_name = value_str[:i]
        if func_name in _DIRECT_INITIALIZERS and isinstance(
            node.value, _DIRECT_INITIALIZERS[func_name]
        ):
            return calc_inside_rd(value_str)
    return None
