import ast

# ast docs: boolop = And | Or


def handle_bool_op_type(_type: ast.boolop) -> str:
    if isinstance(_type, ast.And):
        return "&&"
    if isinstance(_type, ast.Or):
        return "||"
    # TODO: extract "shouldn't happen" to a common place. And say like
    # "If you see this it is a bug, please report it at ..."
    raise Exception("Shouldn't happen")
