import ast
from pathlib import Path

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.expr import (
    ExprHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_attribute import (
    AttributeHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_bin_op import (
    BinOpHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_bool_op import (
    BoolOpHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_call.h_call import (
    CallHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_compare import (
    CompareHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_constant import (
    ConstantHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_dict import (
    DictHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_if_exp import (
    IfExpHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_joined_string import (
    JoinedStringHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_lambda import (
    LambdaHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_list import (
    ListHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_name import (
    NameHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_set import (
    SetHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_slice import (
    SliceHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_subscript import (
    SubscriptHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_tuple import (
    TupleHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_unary_op import (
    UnaryOpHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_yield import (
    YieldHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_yield_from import (
    YieldFromHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.h_ann_assign import (  # noqa: E501
    handle_ann_assign,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_type_alias import (
    handle_type_alias,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.stmt import (
    handle_stmt,
)
from pypp_cli.src.transpilers.other.transpiler.maps.maps import Maps
from pypp_cli.src.transpilers.other.transpiler.handle_import_stmts import (
    analyse_import_stmts,
)
from pypp_cli.src.transpilers.other.transpiler.cpp_includes import CppIncludes


def handle_imports_and_create_deps(
    module: ast.Module,
    maps: Maps,
    src_py_files: list[Path],
    file_path: Path,
    is_main_file: bool = False,
) -> tuple[int, Deps]:
    cpp_inc_map, import_end, py_imports, user_namespace = analyse_import_stmts(
        module.body, maps, src_py_files, file_path
    )

    d: Deps = Deps(
        file_path,
        CppIncludes(set(), set(), cpp_inc_map),
        [],
        maps,
        py_imports,
        handle_stmt,
        handle_ann_assign,
        handle_type_alias,
        user_namespace,
        is_main_file=is_main_file,
    )
    attribute_handler = AttributeHandler(d)
    bin_op_handler = BinOpHandler(d)
    bool_op_handler = BoolOpHandler(d)
    call_handler = CallHandler(d)
    compare_handler = CompareHandler(d)
    constant_handler = ConstantHandler(d)
    dict_handler = DictHandler(d)
    if_exp_handler = IfExpHandler(d)
    joined_string_handler = JoinedStringHandler(d)
    lambda_handler = LambdaHandler(d)
    list_handler = ListHandler(d)
    name_handler = NameHandler(d)
    set_handler = SetHandler(d)
    slice_handler = SliceHandler(d)
    subscript_handler = SubscriptHandler(d)
    tuple_handler = TupleHandler(d)
    unary_op_handler = UnaryOpHandler(d)
    yield_handler = YieldHandler(d)
    yield_from_handler = YieldFromHandler(d)

    expr_handler = ExprHandler(
        d,
        attribute_handler,
        bin_op_handler,
        bool_op_handler,
        call_handler,
        compare_handler,
        constant_handler,
        dict_handler,
        if_exp_handler,
        joined_string_handler,
        lambda_handler,
        list_handler,
        name_handler,
        set_handler,
        slice_handler,
        subscript_handler,
        tuple_handler,
        unary_op_handler,
        yield_handler,
        yield_from_handler,
    )
    d.set_expr_handler(expr_handler)

    return import_end, d


def is_proper_main_block(node: ast.stmt) -> bool:
    if not isinstance(node, ast.If):
        return False
    if len(node.orelse) != 0:
        return False
    if not isinstance(node.test, ast.Compare):
        return False
    if not isinstance(node.test.left, ast.Name):
        return False
    if node.test.left.id != "__name__":
        return False
    if len(node.test.ops) != 1:
        return False
    if not isinstance(node.test.ops[0], ast.Eq):
        return False
    if len(node.test.comparators) != 1:
        return False
    comp = node.test.comparators[0]
    if not isinstance(comp, ast.Constant):
        return False
    if comp.value != "__main__":
        return False
    return True
