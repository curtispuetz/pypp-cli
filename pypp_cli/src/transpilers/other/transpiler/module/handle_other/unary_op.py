import ast

# ast docs: unaryop = Invert | Not | UAdd | USub


def handle_unaryop(_type: ast.unaryop) -> str:
    if isinstance(_type, ast.USub):
        return "-"
    if isinstance(_type, ast.UAdd):
        return "+"
    if isinstance(_type, ast.Not):
        return "!"
    if isinstance(_type, ast.Invert):
        return "~"
    raise Exception("Shouldn't happen")
