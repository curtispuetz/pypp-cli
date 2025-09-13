import ast

from pypp_cli.src.config import SHOULDNT_HAPPEN
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.util.calc_fn_signature import (
    calc_fn_signature,
)

# Underscore rules:
# - If the interface doesn't start with an underscore, then it goes in the header
# file. Otherwise, it goes in the main file.


def handle_class_def_for_interface(node: ast.ClassDef, d: Deps) -> str:
    # Note: interfaces are not supported yet.
    class_name: str = node.name
    is_all_header: bool = not class_name.startswith("_")

    d.set_inc_in_h(is_all_header)
    body_list = _calc_methods(node, d)
    d.set_inc_in_h(False)

    body_list.append(_calc_destructor(class_name))
    body_str: str = " ".join(body_list)
    result = f"class {class_name} " + "{" + f"public: {body_str}" + "};\n\n"
    if is_all_header:
        d.ret_h_file.append(result)
        return ""
    return result


def _calc_methods(node: ast.ClassDef, d: Deps) -> list[str]:
    ret: list[str] = []
    for item in node.body:
        # Shouldn't happen because Because this was already checked
        assert isinstance(item, ast.FunctionDef), SHOULDNT_HAPPEN
        fn_signature = calc_fn_signature(
            item,
            d,
            item.name,
            skip_first_arg=True,  # because it is self
        )
        ret.append("virtual " + fn_signature + " = 0;")
    return ret


def _calc_destructor(class_name: str) -> str:
    # GPT 4.1 recommended that you have a destructor these these 'interface type'
    # classes
    return f"virtual ~{class_name}() " + "{}"
