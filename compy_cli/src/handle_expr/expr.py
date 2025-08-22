import ast

from compy_cli.src.deps import Deps
from compy_cli.src.handle_expr.h_attribute import handle_attribute
from compy_cli.src.handle_expr.h_bin_op import handle_bin_op
from compy_cli.src.handle_expr.h_call.h_call import handle_call
from compy_cli.src.handle_expr.h_compare import handle_compare
from compy_cli.src.handle_expr.h_constant import handle_constant
from compy_cli.src.handle_expr.h_dict import handle_dict
from compy_cli.src.handle_expr.h_joined_string import handle_joined_string
from compy_cli.src.handle_expr.h_lambda import handle_lambda
from compy_cli.src.handle_expr.h_list import handle_list
from compy_cli.src.handle_expr.h_name import handle_name
from compy_cli.src.handle_expr.h_set import handle_set
from compy_cli.src.handle_expr.h_subscript import handle_subscript
from compy_cli.src.handle_expr.h_tuple import handle_tuple
from compy_cli.src.handle_expr.h_unary_op import handle_unary_op
from compy_cli.src.handle_expr.h_slice import handle_slice
from compy_cli.src.handle_expr.h_yield import handle_yield
from compy_cli.src.handle_expr.h_yield_from import handle_yield_from


def handle_expr(node: ast.expr, d: Deps) -> str:
    if isinstance(node, ast.Compare):
        return handle_compare(node, d)
    if isinstance(node, ast.Name):
        return handle_name(node, d)
    if isinstance(node, ast.Constant):
        return handle_constant(node, d)
    if isinstance(node, ast.Call):
        return handle_call(node, d)
    if isinstance(node, ast.Subscript):
        return handle_subscript(node, d)
    if isinstance(node, ast.List):
        return handle_list(node, d)
    if isinstance(node, ast.Attribute):
        return handle_attribute(node, d)
    if isinstance(node, ast.UnaryOp):
        return handle_unary_op(node, d)
    if isinstance(node, ast.Slice):
        return handle_slice(node, d)
    if isinstance(node, ast.BinOp):
        return handle_bin_op(node, d)
    if isinstance(node, ast.Tuple):
        return handle_tuple(node, d)
    if isinstance(node, ast.Dict):
        return handle_dict(node, d)
    if isinstance(node, ast.Set):
        return handle_set(node, d)
    if isinstance(node, ast.JoinedStr):
        return handle_joined_string(node, d)
    if isinstance(node, ast.Lambda):
        return handle_lambda(node, d)
    if isinstance(node, ast.Yield):
        return handle_yield(node, d)
    if isinstance(node, ast.YieldFrom):
        return handle_yield_from(node, d)
    if isinstance(node, ast.Starred):
        raise Exception(
            "Starred expressions are only supported if they are the only argument in a "
            "call"
        )
    if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp)):
        raise Exception("Shouldn't happen. This should be called from ann_assign")
    if isinstance(node, ast.GeneratorExp):
        raise Exception("Generator expressions are not supported")
    raise Exception(f"code expr type {node} not handled")
