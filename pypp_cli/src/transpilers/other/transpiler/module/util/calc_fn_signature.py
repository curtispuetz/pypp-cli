import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.mapping.fn_arg import (
    lookup_cpp_fn_arg,
)
from pypp_cli.src.transpilers.other.transpiler.module.util.calc_callable_type import (
    calc_callable_type,
)
from pypp_cli.src.transpilers.other.transpiler.module.util.inner_strings import (
    calc_inside_sq,
)


def calc_fn_signature(
    node: ast.FunctionDef,
    d: Deps,
    fn_name: str,
    skip_first_arg: bool = False,
) -> str:
    cpp_ret_type: str
    if node.returns is None:
        cpp_ret_type = "void"
    else:
        cpp_ret_type = d.handle_expr(node.returns)
        if cpp_ret_type.startswith("Iterator[") and cpp_ret_type.endswith("]"):
            d.add_inc(QInc("pypp_util/generator.h"))
            cpp_ret_type = f"Generator<{calc_inside_sq(cpp_ret_type)}>"
        elif cpp_ret_type.startswith("&"):
            cpp_ret_type = cpp_ret_type[1:] + "&"
    cpp_args_str = _calc_cpp_args_str(node, d, skip_first_arg)
    return f"{cpp_ret_type} {fn_name}({cpp_args_str})"


def _calc_cpp_args_str(
    node: ast.FunctionDef,
    d: Deps,
    skip_first_arg: bool = False,
) -> str:
    ret: list[str] = []
    cpp_arg_types = calc_fn_arg_types(node, d, skip_first_arg)
    for n, t in cpp_arg_types.items():
        ret.append(f"{t} {n}")
    return ", ".join(ret)


def calc_fn_arg_types(
    node: ast.FunctionDef,
    d: Deps,
    skip_first_arg: bool = False,
) -> dict[str, str]:
    ret = {}
    for i in range(skip_first_arg, len(node.args.args)):
        py_arg = node.args.args[i]
        arg_name: str = py_arg.arg
        assert py_arg.annotation is not None, (
            f"function argument {arg_name} must have type annotation"
        )
        cpp_arg_type: str | None = calc_callable_type(py_arg.annotation, d)
        if cpp_arg_type is None:
            cpp_arg_type = d.handle_expr(py_arg.annotation)
        cpp_arg = lookup_cpp_fn_arg(cpp_arg_type, d)
        ret[arg_name] = cpp_arg
    return ret


def calc_fn_str_with_body(fn_signature: str, body_str: str) -> str:
    return f"{fn_signature} " + "{" + body_str + "}\n\n"
