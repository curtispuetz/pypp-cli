import ast
from dataclasses import dataclass

from pypp_cli.do.z_i.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.z_i.d_types import QInc
from pypp_cli.do.transpile.transpile.handle.z.deps import Deps
from pypp_cli.do.transpile.transpile.handle.z.handlers.handle_expr.h_constant import (
    SPECIAL_CHAR_MAP,
)


@dataclass(frozen=True, slots=True)
class JoinedStringHandler:
    _d: Deps

    def handle(self, node: ast.JoinedStr) -> str:
        self._d.add_inc(QInc("py_str.h"))
        std_format_args: list[str] = []
        std_format_first_arg: list[str] = []
        for n in node.values:
            if isinstance(n, ast.Constant):
                assert isinstance(n.value, str), SHOULDNT_HAPPEN
                std_format_first_arg.append(n.value)
            else:
                assert isinstance(n, ast.FormattedValue), SHOULDNT_HAPPEN
                std_format_first_arg.append("{}")
                std_format_args.append(self._handle_formatted_value(n))
        first_arg_str: str = "".join(std_format_first_arg).translate(SPECIAL_CHAR_MAP)
        args_str: str = ", ".join(std_format_args)
        return f'pypp::PyStr(std::format("{first_arg_str}", {args_str}))'

    def _handle_formatted_value(self, node: ast.FormattedValue) -> str:
        if node.conversion != -1:
            self._d.value_err(
                "f-string conversion flags (i.e. '!r', '!a', '!s') are not supported",
                node,
            )
        if node.format_spec is not None:
            self._d.value_err(
                "Format specifications in f-strings (e.g. ':.2f', etc.) not supported",
                node,
            )
        return self._d.handle_expr(node.value)
