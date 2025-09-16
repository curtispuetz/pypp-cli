import ast
from pathlib import Path
from pypp_cli.src.transpilers.library.transpiler.deps import Deps
from pypp_cli.src.transpilers.library.transpiler.module.mapping.cpp_type import (
    CppTypeCalculator,
)
from ...module.handle_other.operator import OperatorHandler
from ...module.handle_other.with_item import WithItemHandler
from ...module.handle_stmt.h_class_def.for_dataclasses.create_final_str import (
    DataclassFinalStrCreator,
)
from ...module.handle_stmt.h_class_def.for_dataclasses.method_calculator import (
    MethodCalculator,
)
from ...module.util.calc_callable_type import CallableTypeCalculator
from ...module.util.calc_fn_signature import FnSignatureCalculator
from ...module.handle_other.exception_handler import ExceptionHandlersHandler
from ...module.handle_expr.expr import ExprHandler
from ...module.handle_expr.h_attribute import AttributeHandler
from ...module.handle_expr.h_bin_op import BinOpHandler
from ...module.handle_expr.h_bool_op import BoolOpHandler
from ...module.handle_expr.h_call.h_call import CallHandler
from ...module.handle_expr.h_comp import CompHandler
from ...module.handle_expr.h_compare import CompareHandler
from ...module.handle_expr.h_constant import ConstantHandler
from ...module.handle_expr.h_dict import DictHandler
from ...module.handle_expr.h_if_exp import IfExpHandler
from ...module.handle_expr.h_joined_string import JoinedStringHandler
from ...module.handle_expr.h_lambda import LambdaHandler
from ...module.handle_expr.h_list import ListHandler
from ...module.handle_expr.h_name import NameHandler
from ...module.handle_expr.h_set import SetHandler
from ...module.handle_expr.h_slice import SliceHandler
from ...module.handle_expr.h_subscript import SubscriptHandler
from ...module.handle_expr.h_tuple import TupleHandler
from ...module.handle_expr.h_unary_op import UnaryOpHandler
from ...module.handle_expr.h_yield import YieldHandler
from ...module.handle_expr.h_yield_from import YieldFromHandler
from pypp_cli.src.transpilers.library.transpiler.maps.maps import Maps
from .handle_import_stmts import analyse_import_stmts
from pypp_cli.src.transpilers.library.transpiler.cpp_includes import CppIncludes
from ...module.handle_stmt.h_ann_assign.general import GeneralAnnAssignHandler
from ...module.handle_stmt.h_ann_assign.h_ann_assign import AnnAssignHandler
from ...module.handle_stmt.h_assert import AssertHandler
from ...module.handle_stmt.h_assign import AssignHandler
from ...module.handle_stmt.h_aug_assign import AugAssignHandler
from ...module.handle_stmt.h_class_def.for_configclass import (
    ConfigClassHandler,
)
from ...module.handle_stmt.h_class_def.for_dataclasses.calc_fields_and_methods import (
    FieldsAndMethodsCalculator,
)
from ...module.handle_stmt.h_class_def.for_dataclasses.for_dataclasses import (
    DataclassHandler,
)
from ...module.handle_stmt.h_class_def.for_exception import ExceptionClassHandler
from ...module.handle_stmt.h_class_def.for_interface import InterfaceHandler
from ...module.handle_stmt.h_class_def.h_class_def import ClassDefHandler
from ...module.handle_stmt.h_expr import ExprStmtHandler
from ...module.handle_stmt.h_fn_def import FnDefHandler
from ...module.handle_stmt.h_for import ForHandler
from ...module.handle_stmt.h_if import IfHandler
from ...module.handle_stmt.h_raise import RaiseHandler
from ...module.handle_stmt.h_return import ReturnHandler
from ...module.handle_stmt.h_try import TryHandler
from ...module.handle_stmt.h_type_alias import TypeAliasHandler
from ...module.handle_stmt.h_while import WhileHandler
from ...module.handle_stmt.h_with import WithHandler
from ...module.handle_stmt.stmt import StmtHandler


def create_all_transpiler_data(
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
    operator_handler = OperatorHandler(d)
    bin_op_handler = BinOpHandler(d, operator_handler)
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
    aug_assign_handler = AugAssignHandler(d, operator_handler)
    expr_stmt_handler = ExprStmtHandler(d)
    callable_type_calculator = CallableTypeCalculator(d)
    cpp_type_calculator = CppTypeCalculator(d)
    fn_signature_calculator = FnSignatureCalculator(
        d, callable_type_calculator, cpp_type_calculator
    )
    fn_def_handler = FnDefHandler(d, fn_signature_calculator)
    for_handler = ForHandler(d)
    if_handler = IfHandler(d)
    raise_handler = RaiseHandler(d)
    return_handler = ReturnHandler(d)
    exception_handlers_handler = ExceptionHandlersHandler(d)
    try_handler = TryHandler(d, exception_handlers_handler)
    type_alias_handler = TypeAliasHandler(d)
    while_handler = WhileHandler(d)
    with_item_handler = WithItemHandler(d)
    with_handler = WithHandler(d, with_item_handler)
    comp_handler = CompHandler(d, for_handler)
    general_ann_assign_handler = GeneralAnnAssignHandler(
        d, comp_handler, callable_type_calculator
    )
    ann_assign_handler = AnnAssignHandler(d, general_ann_assign_handler)
    interface_handler = InterfaceHandler(d, fn_signature_calculator)
    config_class_handler = ConfigClassHandler(
        d, assign_handler, general_ann_assign_handler
    )
    exception_class_handler = ExceptionClassHandler(d)
    method_calculator = MethodCalculator(d, fn_signature_calculator)
    fields_and_methods_calculator = FieldsAndMethodsCalculator(
        d, method_calculator, cpp_type_calculator
    )
    dataclass_final_str_creator = DataclassFinalStrCreator(d)
    dataclass_handler = DataclassHandler(
        d, fields_and_methods_calculator, dataclass_final_str_creator
    )
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
