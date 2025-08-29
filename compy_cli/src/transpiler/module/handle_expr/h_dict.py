import ast

from compy_cli.src.transpiler.module.deps import Deps


def handle_dict(node: ast.Dict, d: Deps) -> str:
    ret: list[str] = []
    assert len(node.keys) == len(node.values), "Shouldn't happen"
    for k_node, v_node in zip(node.keys, node.values):
        if k_node is None:
            raise ValueError(
                "dictionary literals in dict declaration "
                "(e.g. {0: 1, **a}) not supported "
            )
        k = d.handle_expr(k_node)
        v = d.handle_expr(v_node)
        ret.append("{" + f"{k}, {v}" + "}")
    return "{" + ", ".join(ret) + "}"
