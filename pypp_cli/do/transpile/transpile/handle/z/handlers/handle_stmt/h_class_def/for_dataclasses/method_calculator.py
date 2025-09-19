from pypp_cli.do.transpile.transpile.handle.node import Deps
from pypp_cli.do.transpile.transpile.handle.z.handlers.util.calc_fn_signature import (
    FnSignatureCalculator,
)


import ast
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ClassMethod:
    fn_signature: str
    body_str: str
    name: str


@dataclass(frozen=True, slots=True)
class MethodCalculator:
    _d: Deps
    _fn_signature_calculator: FnSignatureCalculator

    def calc(self, node: ast.FunctionDef, is_def_in_header: bool) -> ClassMethod:
        if node.name.startswith("__") and node.name.endswith("__"):
            self._d.value_err_no_ast(
                f"magic method '{node.name}' for a class is not supported"
            )
        if node.args.args[0].arg != "self":
            self._d.value_err_no_ast(
                "first argument of a method must be 'self'. Problem method: "
                + node.name
            )

        fn_signature = self._fn_signature_calculator.calc(
            node,
            node.name,
            skip_first_arg=True,  # because it is self
        )
        self._d.set_inc_in_h(False)
        body_str: str = self._d.handle_stmts(node.body)
        self._d.set_inc_in_h(is_def_in_header)

        return ClassMethod(fn_signature, body_str, node.name)
