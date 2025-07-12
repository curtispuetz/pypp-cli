import ast

from src.util.calc_fn_signature import calc_fn_signature
from src.util.ret_imports import RetImports


def handle_class_def_for_interface(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
) -> str:
    # Note: interfaces are not supported yet.
    class_name: str = node.name
    name_doesnt_start_with_underscore: bool = not class_name.startswith("_")
    body_list = _calc_methods(
        node,
        ret_imports,
        handle_expr,
        name_doesnt_start_with_underscore,
    )
    body_list.append(_calc_destructor(class_name))
    body_str: str = " ".join(body_list)
    result = f"class {class_name} " + "{" + f"public: {body_str}" + "};\n\n"
    if name_doesnt_start_with_underscore:
        ret_h_file.append(result)
        return ""
    return result


def _calc_methods(
    node: ast.ClassDef,
    ret_imports: RetImports,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> list[str]:
    ret: list[str] = []
    for item in node.body:
        # Note: assertions have already been done.
        fn_signature = calc_fn_signature(
            item,
            ret_imports,
            handle_expr,
            item.name,
            name_doesnt_start_with_underscore,
            skip_first_arg=True,  # because it is self
        )
        ret.append("virtual " + fn_signature + " = 0;")
    return ret


def _calc_destructor(class_name: str) -> str:
    # GPT 4.1 recommended that you have a destructor these these 'interface type'
    # classes
    return f"virtual ~{class_name}() " + "{}"
