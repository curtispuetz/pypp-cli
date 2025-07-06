import ast

from src.util.ret_imports import RetImports


def handle_type_alias(
    node: ast.TypeAlias,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
) -> str:
    name: str = handle_expr(node.name, ret_imports)
    name_starts_with_underscore: bool = name.startswith("_")
    value: str = handle_expr(
        node.value, ret_imports, include_in_header=not name_starts_with_underscore
    )
    assert len(node.type_params) == 0, "type parameters for type alias not supported"
    res: str = f"using {name} = {value};"
    if name_starts_with_underscore:
        return res
    # In the header file if name does not start with an underscore
    ret_h_file.append(res)
    return ""
