import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_attribute import (
    handle_attribute,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_bin_op import (
    handle_bin_op,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_call.h_call import (
    handle_call,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_compare import (
    handle_compare,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_constant import (
    handle_constant,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_dict import (
    handle_dict,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_if_exp import (
    handle_if_exp,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_joined_string import (  # noqa: E501
    handle_joined_string,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_lambda import (
    handle_lambda,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_list import (
    handle_list,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_name import (
    handle_name,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_set import (
    handle_set,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_subscript import (
    handle_subscript,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_tuple import (
    handle_tuple,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_unary_op import (
    handle_unary_op,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_slice import (
    handle_slice,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_yield import (
    handle_yield,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_yield_from import (
    handle_yield_from,
)


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
    if isinstance(node, ast.IfExp):
        return handle_if_exp(node, d)
    if isinstance(node, ast.Starred):
        d.value_err(
            "Starred expressions are not supported",
            node,
        )
    if isinstance(node, ast.ListComp):
        d.value_err(
            "List comprehensions are only supported with assignment to a variable.",
            node,
        )
    if isinstance(node, ast.SetComp):
        d.value_err(
            "Set comprehensions are only supported with assignment to a variable.",
            node,
        )
    if isinstance(node, ast.DictComp):
        d.value_err(
            "Dict comprehensions are only supported with assignment to a variable.",
            node,
        )
    if isinstance(node, ast.GeneratorExp):
        d.value_err("Generator expressions are not supported", node)
    d.value_err(f"code expr type {node} not supported", node)
