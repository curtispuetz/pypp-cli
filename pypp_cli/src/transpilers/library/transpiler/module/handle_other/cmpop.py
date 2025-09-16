import ast

from pypp_cli.src.config import SHOULDNT_HAPPEN

# ast docs: cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn


def handle_cmpop(_type: ast.cmpop) -> str:
    if isinstance(_type, ast.Eq):
        return "=="
    if isinstance(_type, ast.NotEq):
        return "!="
    if isinstance(_type, ast.Lt):
        return "<"
    if isinstance(_type, ast.LtE):
        return "<="
    if isinstance(_type, ast.Gt):
        return ">"
    if isinstance(_type, ast.GtE):
        return ">="
    # NOTE: all types are handled (In, NotIn, Is, IsNot are handled before the
    #  function call)
    raise Exception(SHOULDNT_HAPPEN)
