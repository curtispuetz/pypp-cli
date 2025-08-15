import ast

from pypp_core.src.deps import Deps


def handle_dict(
    node: ast.Dict,
    d: Deps,
    include_in_header: bool,
) -> str:
    ret: list[str] = []
    assert len(node.keys) == len(node.values), "Shouldn't happen"
    for k_node, v_node in zip(node.keys, node.values):
        if k_node is None:
            raise ValueError(
                "dictionary literals in dict declaration "
                "(e.g. {0: 1, **a}) not supported "
            )
        k = d.handle_expr(k_node, include_in_header)
        v = d.handle_expr(v_node, include_in_header)
        ret.append("{" + f"{k}, {v}" + "}")
    return "{" + ", ".join(ret) + "}"
