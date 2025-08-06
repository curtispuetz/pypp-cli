import ast

from src.deps import Deps


def handle_dict(
    node: ast.Dict,
    d: Deps,
    include_in_header: bool,
) -> str:
    ret: list[str] = []
    assert len(node.keys) == len(node.values), "Shouldn't happen"
    for k_node, v_node in zip(node.keys, node.values):
        k = d.handle_expr(k_node, include_in_header)
        v = d.handle_expr(v_node, include_in_header)
        ret.append("{" + f"{k}, {v}" + "}")
    return "{" + ", ".join(ret) + "}"
