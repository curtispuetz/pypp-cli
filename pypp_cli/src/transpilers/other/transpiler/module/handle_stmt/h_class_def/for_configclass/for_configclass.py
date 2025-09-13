import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.general import (  # noqa: E501
    handle_general_ann_assign,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_assign import (
    handle_assign,
)

# Underscore rules:
# - If the config class doesn't start with an underscore, then it goes in the header
# file. Otherwise, it goes in the main file.


def handle_class_def_for_configclass(
    node: ast.ClassDef,
    d: Deps,
    dtype: ast.expr | None,
):
    instance_name: str = node.name
    is_all_header: bool = not d.is_main_file and not instance_name.startswith("_")

    d.set_inc_in_h(is_all_header)
    body_str: str
    if dtype is None:
        body_str = _calc_ann_assigns(node, d)
    else:
        body_str = _calc_assigns(node, d, dtype)
    d.set_inc_in_h(False)

    # This is a secret name that won't be used other than to create the instance.
    class_name = f"__PseudoPyppName{instance_name}"
    res: str = (
        f"struct {class_name} "
        + "{"
        + body_str
        + "}; "
        + f"inline {class_name} {instance_name};\n\n"
    )
    if is_all_header:
        d.ret_h_file.append(res)
        return ""
    return res


def _calc_ann_assigns(node: ast.ClassDef, d: Deps) -> str:
    ret: list[str] = []
    for ann_assign in node.body:
        if not isinstance(ann_assign, ast.AnnAssign):
            d.value_err(
                "A configclass without 'dtype' arg should only have assignments with "
                "annotations in the class body",
                ann_assign,
            )
        ret.append(
            handle_general_ann_assign(ann_assign, d, d.handle_expr(ann_assign.target))
        )
    return " ".join(ret)


def _calc_assigns(
    node: ast.ClassDef,
    d: Deps,
    dtype: ast.expr,
) -> str:
    dtype_str: str = d.handle_expr(dtype)
    ret: list[str] = []
    for assign in node.body:
        if not isinstance(assign, ast.Assign):
            d.value_err(
                "A configclass with 'dtype' arg should only have assignments without "
                "annotations in the class body",
                assign,
            )
        ret.append(f"{dtype_str} " + handle_assign(assign, d))
    return " ".join(ret)
