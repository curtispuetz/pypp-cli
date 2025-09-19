import ast
from dataclasses import dataclass


from pypp_cli.do.transpile.transpile.y.d_types import AngInc
from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps


def _is_callable_type(node: ast.Subscript) -> bool:
    return isinstance(node.value, ast.Name) and node.value.id == "Callable"


@dataclass(frozen=True, slots=True)
class CallableTypeCalculator:
    _d: Deps

    def calc(self, node: ast.expr) -> str | None:
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "Valu"
        ):
            arg1 = node.args[0]
            if isinstance(arg1, ast.Subscript):
                if _is_callable_type(arg1):
                    return "Valu(" + self._calc_callable_type(arg1) + ")"
        if isinstance(node, ast.Subscript):
            if _is_callable_type(node):
                return self._calc_callable_type(node)
        return None

    def _calc_callable_type(self, node: ast.Subscript) -> str:
        self._d.add_inc(AngInc("functional"))
        if not isinstance(node.slice, ast.Tuple) or len(node.slice.elts) != 2:
            self._d.value_err("2 arguments required for Callable", node)
        arg_types = node.slice.elts[0]
        if not isinstance(arg_types, ast.List):
            self._d.value_err("First argument for Callable must be a List", node)
        arg_types_cpp = self._d.handle_exprs(arg_types.elts)
        ret_type = node.slice.elts[1]
        ret_type_cpp = self._d.handle_expr(ret_type)
        if ret_type_cpp == "std::monostate":
            ret_type_cpp = "void"
        return f"std::function<{ret_type_cpp}({arg_types_cpp})> "
