import ast

from src.util.ret_imports import RetImports


def handle_type_alias(
    node: ast.TypeAlias,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
):
    # TODO: this should go in the h file typically. Actually, for simplicity for now
    #  it will always go in the h file.
    name = handle_expr(node.name, ret_imports)
    value = handle_expr(node.value, ret_imports)
    assert len(node.type_params) == 0, "type parameters for type alias not supported"
    return f"using {name} = {value};"
