import ast
from dataclasses import dataclass

from src.deps import Deps
from src.util.calc_fn_signature import calc_fn_signature
from src.util.handle_lists import handle_stmts


ARG_PREFIX = "a_"


@dataclass(frozen=True, slots=True)
class ClassField:
    type_cpp: str
    target_str: str
    target_other_name: str
    ref: str


@dataclass(frozen=True, slots=True)
class ClassMethod:
    fn_signature: str
    body_str: str


def calc_method(
    node: ast.FunctionDef,
    d: Deps,
    name_doesnt_start_with_underscore: bool,
) -> ClassMethod:
    assert not (node.name.startswith("__") and node.name.endswith("__")), (
        f"magic method {node.name} for a class is not supported"
    )
    assert node.args.args[0].arg == "self", "first arg must be self"
    fn_signature = calc_fn_signature(
        node,
        d,
        node.name,
        name_doesnt_start_with_underscore,
        skip_first_arg=True,  # because it is self
    )
    # TODO: can I just pass d rather than creating a new Deps instance?
    body_str: str = handle_stmts(
        node.body,
        Deps(d.ret_imports, [], d.py_imports, d.handle_expr_fn, d.handle_stmt),
    )
    return ClassMethod(fn_signature, body_str)


def calc_class_field(type_cpp: str, name: str, other_name: str):
    if type_cpp.endswith("&"):
        ref = "&"
        type_cpp = type_cpp[:-1]
    else:
        ref = ""
    return ClassField(type_cpp, name, other_name, ref)
