import ast

from src.d_types import CppInclude


def handle_dict(node: ast.Dict, ret_imports: set[CppInclude], handle_expr) -> str:
    ret: list[str] = []
    assert len(node.keys) == len(node.values), "Shouldn't happen"
    for k_node, v_node in zip(node.keys, node.values):
        k = handle_expr(k_node, ret_imports)
        v = handle_expr(v_node, ret_imports)
        ret.append("{" + f"{k}, {v}" + "}")
    # TODO: check dict works if it isn't an assignment. I think it will only work on
    #  assignments.
    return "{" + ", ".join(ret) + "}"
