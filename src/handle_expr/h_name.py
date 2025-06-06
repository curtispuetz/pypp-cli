import ast


def handle_name(node: ast.Name) -> str:
    return node.id
