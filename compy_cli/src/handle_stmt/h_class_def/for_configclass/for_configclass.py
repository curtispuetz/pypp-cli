import ast

from compy_cli.src.deps import Deps
from compy_cli.src.handle_stmt.h_ann_assign import handle_general_ann_assign
from compy_cli.src.handle_stmt.h_assign import handle_assign


def handle_class_def_for_configclass(
    node: ast.ClassDef,
    d: Deps,
    dtype: ast.expr | None,
):
    instance_name: str = node.name
    name_doesnt_start_with_underscore: bool = not instance_name.startswith("_")
    d.set_inc_in_h(name_doesnt_start_with_underscore)
    body_str: str
    if dtype is None:
        body_str = _calc_ann_assigns(node, d)
    else:
        body_str = _calc_assigns(node, d, dtype)
    d.set_inc_in_h(False)
    # This is a secret name that won't be used other than to create the instance.
    class_name = f"_PseudoPyppName{instance_name}"
    result: str = (
        f"struct {class_name} "
        + "{"
        + body_str
        + "}; "
        + f"inline {class_name} {instance_name};\n\n"
    )
    if name_doesnt_start_with_underscore:
        d.ret_h_file.append(result)
        return ""
    return result


def _calc_ann_assigns(node: ast.ClassDef, d: Deps) -> str:
    ret: list[str] = []
    for ann_assign in node.body:
        assert isinstance(ann_assign, ast.AnnAssign), (
            "configclass without dtype arg should only have assignments with "
            "annotations in body"
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
        assert isinstance(assign, ast.Assign), (
            "configclass dtype arg should only have assignments without annotations "
            "in body"
        )
        ret.append(f"{dtype_str} " + handle_assign(assign, d))
    return " ".join(ret)
