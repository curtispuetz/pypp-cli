import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.node import Deps
from .h_attribute import AttributeHandler
from .h_bin_op import BinOpHandler
from .h_bool_op import BoolOpHandler
from .h_call.h_call import CallHandler
from .h_compare import CompareHandler
from .h_constant import ConstantHandler
from .h_dict import DictHandler
from .h_if_exp import IfExpHandler
from .h_joined_string import JoinedStringHandler
from .h_lambda import LambdaHandler
from .h_list import ListHandler
from .h_name import NameHandler
from .h_set import SetHandler
from .h_subscript import SubscriptHandler
from .h_tuple import TupleHandler
from .h_unary_op import UnaryOpHandler
from .h_slice import SliceHandler
from .h_yield import YieldHandler
from .h_yield_from import YieldFromHandler


@dataclass(frozen=True, slots=True)
class ExprHandler:
    _d: Deps
    _attribute: AttributeHandler
    _bin_op: BinOpHandler
    _bool_op: BoolOpHandler
    _call: CallHandler
    _compare: CompareHandler
    _constant: ConstantHandler
    _dict_handler: DictHandler
    _if_exp: IfExpHandler
    _joined_string: JoinedStringHandler
    _lambda: LambdaHandler
    _list: ListHandler
    _name: NameHandler
    _set: SetHandler
    _slice: SliceHandler
    _subscript: SubscriptHandler
    _tuple: TupleHandler
    _unary_op: UnaryOpHandler
    _yield: YieldHandler
    _yield_from: YieldFromHandler

    def handle(self, node: ast.expr) -> str:
        if isinstance(node, ast.Compare):
            return self._compare.handle(node)
        if isinstance(node, ast.Name):
            return self._name.handle(node)
        if isinstance(node, ast.Constant):
            return self._constant.handle(node)
        if isinstance(node, ast.Call):
            return self._call.handle(node)
        if isinstance(node, ast.Subscript):
            return self._subscript.handle(node)
        if isinstance(node, ast.BoolOp):
            return self._bool_op.handle(node)
        if isinstance(node, ast.List):
            return self._list.handle(node)
        if isinstance(node, ast.Attribute):
            return self._attribute.handle(node)
        if isinstance(node, ast.UnaryOp):
            return self._unary_op.handle(node)
        if isinstance(node, ast.Slice):
            return self._slice.handle(node)
        if isinstance(node, ast.BinOp):
            return self._bin_op.handle(node)
        if isinstance(node, ast.Tuple):
            return self._tuple.handle(node)
        if isinstance(node, ast.Dict):
            return self._dict_handler.handle(node)
        if isinstance(node, ast.Set):
            return self._set.handle(node)
        if isinstance(node, ast.JoinedStr):
            return self._joined_string.handle(node)
        if isinstance(node, ast.Lambda):
            return self._lambda.handle(node)
        if isinstance(node, ast.Yield):
            return self._yield.handle(node)
        if isinstance(node, ast.YieldFrom):
            return self._yield_from.handle(node)
        if isinstance(node, ast.IfExp):
            return self._if_exp.handle(node)
        if isinstance(node, ast.Starred):
            self._d.value_err(
                "Starred expressions are not supported",
                node,
            )
        if isinstance(node, ast.ListComp):
            self._d.value_err(
                "List comprehensions are only supported with assignment to a variable.",
                node,
            )
        if isinstance(node, ast.SetComp):
            self._d.value_err(
                "Set comprehensions are only supported with assignment to a variable.",
                node,
            )
        if isinstance(node, ast.DictComp):
            self._d.value_err(
                "Dict comprehensions are only supported with assignment to a variable.",
                node,
            )
        if isinstance(node, ast.GeneratorExp):
            self._d.value_err("Generator expressions are not supported", node)
        self._d.value_err(f"code expr type {node} not supported", node)
