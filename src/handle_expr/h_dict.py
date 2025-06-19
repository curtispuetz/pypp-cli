import ast

from src.util.ret_imports import RetImports


def handle_dict(
    node: ast.Dict,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
) -> str:
    ret: list[str] = []
    assert len(node.keys) == len(node.values), "Shouldn't happen"
    for k_node, v_node in zip(node.keys, node.values):
        k = handle_expr(k_node, ret_imports, include_in_header)
        v = handle_expr(v_node, ret_imports, include_in_header)
        ret.append("{" + f"{k}, {v}" + "}")
    return "{" + ", ".join(ret) + "}"
