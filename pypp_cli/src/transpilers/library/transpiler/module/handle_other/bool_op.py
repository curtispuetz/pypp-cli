import ast

from pypp_cli.src.config import SHOULDNT_HAPPEN

# ast docs: boolop = And | Or


def handle_bool_op_type(_type: ast.boolop) -> str:
    if isinstance(_type, ast.And):
        return "&&"
    if isinstance(_type, ast.Or):
        return "||"
    raise Exception(SHOULDNT_HAPPEN)
