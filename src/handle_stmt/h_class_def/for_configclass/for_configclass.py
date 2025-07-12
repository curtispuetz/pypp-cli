import ast

from src.handle_stmt.h_ann_assign import handle_general_ann_assign
from src.handle_stmt.h_assign import handle_assign
from src.util.ret_imports import RetImports


def handle_class_def_for_configclass(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
    handle_stmt,
    dtype: ast.expr | None,
):
    instance_name: str = node.name
    name_doesnt_start_with_underscore: bool = not instance_name.startswith("_")
    body_str: str
    if dtype is None:
        body_str = _calc_ann_assigns(
            node,
            ret_imports,
            ret_h_file,
            handle_expr,
            handle_stmt,
            name_doesnt_start_with_underscore,
        )
    else:
        body_str = _calc_assigns(
            node, ret_imports, handle_expr, name_doesnt_start_with_underscore, dtype
        )
    # This is a secret name that won't be used other than to create the instance.
    class_name = f"_PseudoPyppName{instance_name}"
    result: str = (
        f"struct {class_name} "
        + "{"
        + body_str
        + "}; "
        + f"inline {class_name} {instance_name};"
    )
    if name_doesnt_start_with_underscore:
        ret_h_file.append(result)
        return ""
    return result


def _calc_ann_assigns(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
    handle_stmt,
    include_in_header: bool,
) -> str:
    ret: list[str] = []
    for ann_assign in node.body:
        assert isinstance(ann_assign, ast.AnnAssign), (
            "configclass without dtype arg should only have assignments with annotations in body"
        )
        ret.append(
            handle_general_ann_assign(
                ann_assign,
                ret_imports,
                ret_h_file,
                handle_expr,
                handle_stmt,
                handle_expr(ann_assign.target, ret_imports),
                include_in_header,
            )
        )
    return " ".join(ret)


def _calc_assigns(
    node: ast.ClassDef,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
    dtype: ast.expr,
) -> str:
    dtype_str: str = handle_expr(dtype, ret_imports, include_in_header)
    ret: list[str] = []
    for assign in node.body:
        assert isinstance(assign, ast.Assign), (
            "configclass dtype arg should only have assignments without annotations in body"
        )
        ret.append(
            f"{dtype_str} "
            + handle_assign(assign, ret_imports, handle_expr, include_in_header)
        )
    return " ".join(ret)
