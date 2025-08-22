import ast

from compy_cli.src.deps import Deps


def handle_type_alias(node: ast.TypeAlias, d: Deps) -> str:
    name: str = d.handle_expr(node.name)
    name_starts_with_underscore: bool = name.startswith("_")
    d.set_inc_in_h(not name_starts_with_underscore)
    value: str = d.handle_expr(node.value)
    d.set_inc_in_h(False)
    assert len(node.type_params) == 0, "type parameters for type alias not supported"
    res: str = f"using {name} = {value};"
    if name_starts_with_underscore:
        return res
    # In the header file if name does not start with an underscore
    d.ret_h_file.append(res)
    return ""
