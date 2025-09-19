import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.z.deps import Deps
from pypp_cli.do.transpile.transpile.handle.z.handlers.util.calc_fn_signature import (
    FnSignatureCalculator,
    calc_fn_str_with_body,
)


# Underscore rules:
# - If the function starts with an underscore, then; 1) it is not defined in the header
# file and 2) it gets a `static` prefix so that name conflicts can be avoided.


@dataclass(frozen=True, slots=True)
class FnDefHandler:
    _d: Deps
    _fn_signature_calculator: FnSignatureCalculator

    def handle(self, node: ast.FunctionDef) -> str:
        if len(node.decorator_list) != 0:
            self._d.value_err_no_ast(
                f"function decorators are not supported. Problem function: {node.name}"
            )
        fn_name = node.name
        is_header_defined: bool = not fn_name.startswith("_")

        self._d.set_inc_in_h(is_header_defined)
        fn_signature: str = self._fn_signature_calculator.calc(node, fn_name)
        self._d.set_inc_in_h(False)

        if is_header_defined:
            self._d.ret_h_file.append(fn_signature + ";")
        else:
            fn_signature = "static " + fn_signature
        body_str: str = self._d.handle_stmts(node.body)
        return calc_fn_str_with_body(fn_signature, body_str)
