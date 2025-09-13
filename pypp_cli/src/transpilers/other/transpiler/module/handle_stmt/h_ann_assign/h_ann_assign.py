import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.general import (  # noqa: E501
    handle_general_ann_assign,
)

# Underscore and ALL_CAPS rules:
# - If the ann assign is at module level and does not start with an underscore, then it
# goes in the header file with `inline` prefix.
# - If the ann assign is ALL_CAPS, then it gets a `const` prefix


def handle_ann_assign(
    node: ast.AnnAssign, d: Deps, is_module_level: bool = False
) -> str:
    target_str: str = d.handle_expr(node.target)

    is_header_only: bool = is_module_level and not target_str.startswith("_")

    prefix_str = _calc_prefix_str(is_header_only, target_str)

    d.set_inc_in_h(is_header_only)
    result: str = handle_general_ann_assign(
        node,
        d,
        target_str,
        prefix_str,
    )
    d.set_inc_in_h(False)

    if is_header_only:
        d.ret_h_file.append(result)
        return ""
    return result


def _calc_prefix_str(is_header_only: bool, target_str: str) -> str:
    is_const: bool = target_str.isupper()
    h_str: str = "inline " if is_header_only else ""
    const_str: str = "const " if is_const else ""
    return h_str + const_str
