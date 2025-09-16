import ast
from dataclasses import dataclass
from logging import Handler, config
from pathlib import Path

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.maps import ann_assign
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
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_comp import (
    CompHandler,
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
from pypp_cli.src.transpilers.other.transpiler.maps.maps import Maps
from pypp_cli.src.transpilers.other.transpiler.handle_import_stmts import (
    analyse_import_stmts,
)
from pypp_cli.src.transpilers.other.transpiler.cpp_includes import CppIncludes
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.general import (
    GeneralAnnAssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.h_ann_assign import (
    AnnAssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_assert import (
    AssertHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_assign import (
    AssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_aug_assign import (
    AugAssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_configclass.for_configclass import (
    ConfigClassHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_dataclasses.for_dataclasses import (
    DataclassHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_exception import (
    ExceptionClassHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_interface.for_interface import (
    InterfaceHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.h_class_def import (
    ClassDefHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_expr import (
    ExprStmtHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_fn_def import (
    FnDefHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_for import (
    ForHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_if import IfHandler
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_raise import (
    RaiseHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_return import (
    ReturnHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_try import (
    TryHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_type_alias import (
    TypeAliasHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_while import (
    WhileHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_with import (
    WithHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.stmt import (
    StmtHandler,
)


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

    assert_handler = AssertHandler(d)
    assign_handler = AssignHandler(d)
    aug_assign_handler = AugAssignHandler(d)
    expr_stmt_handler = ExprStmtHandler(d)
    fn_def_handler = FnDefHandler(d)
    for_handler = ForHandler(d)
    if_handler = IfHandler(d)
    raise_handler = RaiseHandler(d)
    return_handler = ReturnHandler(d)
    try_handler = TryHandler(d)
    type_alias_handler = TypeAliasHandler(d)
    while_handler = WhileHandler(d)
    with_handler = WithHandler(d)
    comp_handler = CompHandler(d, for_handler)
    general_ann_assign_handler = GeneralAnnAssignHandler(d, comp_handler)
    ann_assign_handler = AnnAssignHandler(d, general_ann_assign_handler)
    interface_handler = InterfaceHandler(d)
    config_class_handler = ConfigClassHandler(
        d, assign_handler, general_ann_assign_handler
    )
    exception_class_handler = ExceptionClassHandler(d)
    dataclass_handler = DataclassHandler(d)
    class_def_handler = ClassDefHandler(
        d,
        config_class_handler,
        exception_class_handler,
        dataclass_handler,
        interface_handler,
    )
    stmt_handler = StmtHandler(
        d,
        assert_handler,
        assign_handler,
        aug_assign_handler,
        expr_stmt_handler,
        fn_def_handler,
        for_handler,
        if_handler,
        raise_handler,
        return_handler,
        try_handler,
        type_alias_handler,
        while_handler,
        with_handler,
        ann_assign_handler,
        class_def_handler,
    )

    d.set_expr_handler(expr_handler)
    d.set_stmt_handler(stmt_handler)
    d.set_ann_assign_handler(ann_assign_handler)
    d.set_type_alias_handler(type_alias_handler)

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
