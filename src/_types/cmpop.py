import ast

# ast docs: cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn


def lookup_cmpop(_type: ast.cmpop):
    if isinstance(_type, ast.Gt):
        return ">"
    if isinstance(_type, ast.Lt):
        return "<"
    if isinstance(_type, ast.Eq):
        return "=="
    raise f"cmpop type {_type} is not handled"
