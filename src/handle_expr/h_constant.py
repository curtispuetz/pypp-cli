import ast


def handle_constant(node: ast.Constant) -> str:
    if isinstance(node.value, str):
        return f'"{node.value}"'
    if isinstance(node.value, int):
        return str(node.value)
    raise Exception(f"constant type {node.value} not handled")
