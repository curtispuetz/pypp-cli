import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.general import (  # noqa: E501
    handle_general_ann_assign,
)


def handle_ann_assign(node: ast.AnnAssign, d: Deps) -> str:
    target_str: str = d.handle_expr(node.target)
    is_const: bool = target_str.isupper()
    const_str: str = "const " if is_const else ""
    is_private: bool = target_str.startswith("_")
    is_header_only: bool = is_const and not is_private
    d.set_inc_in_h(is_header_only)
    if is_header_only and is_const:
        const_str = "inline const "
    result: str = handle_general_ann_assign(
        node,
        d,
        target_str,
        const_str,
    )
    d.set_inc_in_h(False)
    if is_header_only:
        d.ret_h_file.append(result)
        return ""
    return result
