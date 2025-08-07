import ast

from pypp_core.src.deps import Deps
from pypp_core.src.util.calc_fn_signature import calc_fn_signature


def handle_class_def_for_interface(node: ast.ClassDef, d: Deps) -> str:
    # Note: interfaces are not supported yet.
    class_name: str = node.name
    name_doesnt_start_with_underscore: bool = not class_name.startswith("_")
    body_list = _calc_methods(
        node,
        d,
        name_doesnt_start_with_underscore,
    )
    body_list.append(_calc_destructor(class_name))
    body_str: str = " ".join(body_list)
    result = f"class {class_name} " + "{" + f"public: {body_str}" + "};\n\n"
    if name_doesnt_start_with_underscore:
        d.ret_h_file.append(result)
        return ""
    return result


def _calc_methods(
    node: ast.ClassDef,
    d: Deps,
    name_doesnt_start_with_underscore: bool,
) -> list[str]:
    ret: list[str] = []
    for item in node.body:
        # Shouldn't happen because Because this was already checked
        assert isinstance(item, ast.FunctionDef), "Shouldn't happen"
        fn_signature = calc_fn_signature(
            item,
            d,
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
