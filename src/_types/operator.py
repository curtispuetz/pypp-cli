# ast docs: operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
#                  | RShift | BitOr | BitXor | BitAnd | FloorDiv
import ast


def lookup_op(_type: ast.operator):
    if isinstance(_type, ast.Add):
        return "+"
    if isinstance(_type, ast.Sub):
        return "-"
    if isinstance(_type, ast.Mult):
        return "*"
    if isinstance(_type, ast.Div):
        return "/"
    # TODO: handle floor div
    raise f"cmpop type {_type} is not handled"
