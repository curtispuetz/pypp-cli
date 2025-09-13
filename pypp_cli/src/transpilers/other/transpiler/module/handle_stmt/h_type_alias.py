import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps

# Underscore rules:
# - If the type alias is at module level and does not start with an underscore, then it
# goes in the header file.
# - If the type alias is in a Py++ main file, then it just goes in the main file.


def handle_type_alias(
    node: ast.TypeAlias, d: Deps, is_module_level: bool = False
) -> str:
    if len(node.type_params) != 0:
        d.value_err("type parameters for type aliases are not supported", node)

    name: str = d.handle_expr(node.name)

    is_header_only: bool = is_module_level and not name.startswith("_")

    d.set_inc_in_h(is_header_only)
    value: str = d.handle_expr(node.value)
    d.set_inc_in_h(False)

    res: str = f"using {name} = {value};"
    if is_header_only:
        d.ret_h_file.append(res)
        return ""
    return res
