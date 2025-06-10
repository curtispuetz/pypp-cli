import ast

# ast docs: unaryop = Invert | Not | UAdd | USub


def lookup_unary_op(_type: ast.unaryop) -> str:
    if isinstance(_type, ast.USub):
        return "-"
    if isinstance(_type, ast.Not):
        return "!"
    raise Exception(f"unary op type {_type} is not handled")
