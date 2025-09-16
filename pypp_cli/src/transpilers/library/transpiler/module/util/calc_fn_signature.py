import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.library.transpiler.d_types import QInc
from pypp_cli.src.transpilers.library.transpiler.deps import Deps
from pypp_cli.src.transpilers.library.transpiler.module.mapping.cpp_type import (
    CppTypeCalculator,
)
from pypp_cli.src.transpilers.library.transpiler.module.util.calc_callable_type import (
    CallableTypeCalculator,
)
from pypp_cli.src.transpilers.library.transpiler.module.util.inner_strings import (
    calc_inside_sq,
)


def calc_fn_str_with_body(fn_signature: str, body_str: str) -> str:
    return f"{fn_signature} " + "{" + body_str + "}\n\n"


@dataclass(frozen=True, slots=True)
class FnSignatureCalculator:
    _d: Deps
    _callable_type_calculator: CallableTypeCalculator
    _cpp_type_calculator: CppTypeCalculator

    def calc(
        self, node: ast.FunctionDef, fn_name: str, skip_first_arg: bool = False
    ) -> str:
        cpp_ret_type: str
        if node.returns is None:
            cpp_ret_type = "void"
        else:
            cpp_ret_type = self._d.handle_expr(node.returns)
            if cpp_ret_type.startswith("Iterator[") and cpp_ret_type.endswith("]"):
                self._d.add_inc(QInc("pypp_util/generator.h"))
                cpp_ret_type = f"pypp::Generator<{calc_inside_sq(cpp_ret_type)}>"
            elif cpp_ret_type.startswith("&"):
                cpp_ret_type = cpp_ret_type[1:] + "&"
            elif cpp_ret_type.startswith("Valu(") and cpp_ret_type.endswith(")"):
                self._d.value_err(
                    "Wrapping a return type in `Valu()` is not supported since it has "
                    "no meaning. Remove the `Valu()`.",
                    node.returns,
                )
        cpp_args_str = self._calc_cpp_args_str(node, skip_first_arg)
        return f"{cpp_ret_type} {fn_name}({cpp_args_str})"

    def _calc_cpp_args_str(
        self,
        node: ast.FunctionDef,
        skip_first_arg: bool = False,
    ) -> str:
        ret: list[str] = []
        cpp_arg_types = self._calc_fn_arg_types(node, skip_first_arg)
        for n, t in cpp_arg_types.items():
            ret.append(f"{t} {n}")
        return ", ".join(ret)

    def _calc_fn_arg_types(
        self,
        node: ast.FunctionDef,
        skip_first_arg: bool = False,
    ) -> dict[str, str]:
        ret = {}
        self._assert_args(node.args)
        for i in range(skip_first_arg, len(node.args.args)):
            py_arg = node.args.args[i]
            arg_name: str = py_arg.arg
            if py_arg.annotation is None:
                self._d.value_err(
                    f"function argument '{arg_name}' must have type annotation",
                    py_arg,
                )
            cpp_arg_type: str | None = self._callable_type_calculator.calc(
                py_arg.annotation
            )
            if cpp_arg_type is None:
                cpp_arg_type = self._d.handle_expr(py_arg.annotation)
            ret[arg_name] = self._cpp_type_calculator.calc(cpp_arg_type)
        return ret

    def _assert_args(self, args: ast.arguments):
        if len(args.defaults) != 0:
            self._d.value_err(
                "default function/method arguments are not supported", args
            )
        if args.vararg is not None:
            args.vararg.arg
            self._d.value_err(
                f"A variable amount of arguments '*{args.vararg.arg}' is not supported",
                args,
            )
        if args.kwarg is not None:
            self._d.value_err(
                f"A variable amount of keyword arguments '**{args.kwarg.arg}' is not "
                f"supported",
                args,
            )
        if len(args.kwonlyargs) != 0 or len(args.kw_defaults) != 0:
            self._d.value_err("keyword only arguments are not supported", args)
