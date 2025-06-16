import ast

# ast docs: unaryop = Invert | Not | UAdd | USub


# TODO: instead of calling these 'lookup' I should call them 'handle' just like the
#  other handles. and call. Also rename this directory to types_
def lookup_unary_op(_type: ast.unaryop) -> str:
    if isinstance(_type, ast.USub):
        return "-"
    if isinstance(_type, ast.Not):
        return "!"
    raise Exception(f"unary op type {_type} is not handled")
