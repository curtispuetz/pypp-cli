from pypp_python import configclass, exception, Valu, dataclass
from abc import ABC, abstractmethod
from src.custom_libs.pure_lib_test_0.first import pure_lib_test_0_fn
from src.args_test import args_test_fn
from src.augment_operations import augment_operations_fn
from src.benchmarking import perlin_noise_fn
from src.built_in_functions.dict_fn import built_in_dict_fn
from src.built_in_functions.list_fn import built_in_list_fn
from src.built_in_functions.number_conversions import number_conversions_fn
from src.built_in_functions.set_fn import built_in_set_fn
from src.custom_libs.bridge_lib_test_0.first import bridge_lib_test_0_fn
from src.custom_libs.bridge_lib_test_1.first import bridge_lib_test_1_fn
from src.dataclasses_test.nested_dependencies import dataclass_nested_dependencies_fn
from src.default_dict.create_with_defaults import default_dict_create_with_defaults
from src.default_dict.methods import default_dict_methods_fn
from src.default_dict.operations import default_dict_operations_fn
from src.dicts.looping import dict_looping_fn
from src.dicts.operations import dict_operations_fn
from src.empty_return import empty_return_fn
from src.exceptions.custom_exceptions import custom_exception_fn
from src.exceptions.test_all import test_all_exceptions_fn
from src.file_io.shutil_exceptions import shutil_exceptions_fn
from src.file_io.test_is_here import test_is_here_fn
from src.first import return_something
from src.imports_test.first import imports_test_fn
from src.imports_test.second import imports_test_fn2
from src.inconsistent_behviour.reassigning_a_ref import reassigning_a_ref_fn
from src.interfaces.with_dataclasses import interface_with_dataclasses_fn
from src.lambdas import lambdas_fn
from src.lists.ownership import list_ownership_tests_fn
from src.number_types.in_collections import number_types_in_collections_fn
from src.pass_by_value import pass_by_value_test_fn
from src.random_library.first import random_fn
from src.second import return_friend
from src.sets.operations import set_operations_fn
from src.subscriptable_types import subscriptable_types_fn
from src.third import using_inline_string
from src.fourth import string_as_argument
from src.if_elif_else.if_elif_else import if_elif_else_fn
from src.lists.lists import list_fn
from src.strings.first import string_ops
from src.numbers_test.first import number_ops
from src.lists.as_arg import list_as_arg, list_as_mutable_arg
from src.dicts.first import dict_fn
from src.tuples.first import tuples_fn
from src.sets.first import set_fn
from src.loops.for_ import for_loop_fn
from src.loops.while_ import while_loop_fn
from src.exceptions.throw_ import throw_fn
from src.dicts.exceptions import dict_exceptions_fn
from src.lists.exceptions import list_exceptions_fn
from src.sets.exceptions import set_exceptions_fn
from src.strings.exceptions import string_exceptions_fn
from src.tuples.exceptions import tuple_exceptions_fn
from src.file_io.first import file_io_fn
from src.strings.special_characters import string_esc_chars_fn
from src.strings.f_strings import f_strings_fn
from src.ranges.first import ranges_fn
from src.slices.first import slices_fn
from src.inconsistent_behviour.editing_a_reference import editing_a_reference_fn
from src.loops.enumerate_ import enumerate_fn
from src.printing.first import printing_fn
from src.loops.zip_ import zip_fn
from src.loops.reversed_ import reversed_fn
from src.lists.comprehensions import list_comprehension_fn
from src.sets.comprehensions import set_comprehension_fn
from src.dicts.comprehensions import dict_comprehension_fn
from src.exceptions.assert_ import assert_fn
from src.type_aliases import type_aliases_fn
from src.yields.first import yield_fn
from src.math_library.first import math_library_fn
from src.time_library.first import time_library_fn
from src.sets.of_tuples import set_of_tuples_fn
from src.ref_vars import ref_vars_fn
from src.dataclasses_test.first import dataclass_fn
from src.dataclasses_test.with_methods import dataclass_with_methods_fn
from src.interfaces.first import interfaces_fn
from src.operations import operations_fn
from src.fn_as_vars.first import fn_as_vars_fn
from src.default_dict.first import default_dict_fn
from src.pypp_union.first import pypp_union_fn
from src.constants import constant_fn, A, B, C, D, E, a, b
from src.number_types.number_types import number_types_fn
from src.triple_quote_strings import triple_quote_strings_fn
from src.ternary_op import ternary_op_fn
from src.lists.declaration import list_declaration_fn
from src.lists.operations import list_operations_fn
from src.using_pass import pass_fn


# Show that functions, all the class types, type aliaes, and ann assigns work in
# Py++ main files.
def _private_fn() -> int:
    return 1


type _int_alias = int
_A_CONST: int = 2


@configclass(dtype=int)
class _AConfigClass:
    x = 0
    y = 1


@exception
class _MyCustom(Exception):
    pass


class _MyCInterface(ABC):
    @abstractmethod
    def a(self):
        pass


@dataclass
class MyDataClassInMain:
    my_list: Valu(list[int])

    def calc_something(self) -> list[int]:
        return self.my_list * 4


if __name__ == "__main__":
    print(_A_CONST)
    print(_AConfigClass.x)
    print(MyDataClassInMain([1, 2, 3]).calc_something())
    print(_private_fn())
    print(return_something(1, 9))
    print(return_friend())
    print(using_inline_string())
    print(string_as_argument("hello"))
    print(if_elif_else_fn(6, 6))
    number_ops()
    my_list: list[int] = [1, 2, 3, 4]
    list_as_arg(my_list)
    list_as_mutable_arg(my_list)
    print(my_list)
    str_list: list[str] = ["ab", "cd"]
    print(str_list)
    string_ops()
    set_fn()
    for_loop_fn()
    while_loop_fn()
    throw_fn()
    dict_exceptions_fn()
    list_exceptions_fn()
    set_exceptions_fn()
    string_exceptions_fn()
    tuple_exceptions_fn()
    string_esc_chars_fn()
    f_strings_fn()
    ranges_fn()
    slices_fn()
    editing_a_reference_fn()
    enumerate_fn()
    printing_fn()
    zip_fn()
    reversed_fn()
    file_io_fn()
    set_comprehension_fn()
    dict_comprehension_fn()
    list_comprehension_fn()
    assert_fn()
    type_aliases_fn()
    yield_fn()
    math_library_fn()
    tuples_fn()
    set_of_tuples_fn()
    ref_vars_fn()
    dict_fn()
    dataclass_fn()
    dataclass_with_methods_fn()
    interfaces_fn()
    operations_fn()
    fn_as_vars_fn()
    pypp_union_fn()
    constant_fn()
    imports_test_fn()
    imports_test_fn2()
    number_types_fn()
    time_library_fn()
    default_dict_fn()
    random_fn()
    # perlin_noise_fn()
    custom_exception_fn()
    args_test_fn()
    subscriptable_types_fn()
    lambdas_fn()
    bridge_lib_test_0_fn()
    bridge_lib_test_1_fn()
    list_ownership_tests_fn()
    list_fn()
    dataclass_nested_dependencies_fn()
    triple_quote_strings_fn()
    number_types_in_collections_fn()
    test_is_here_fn()
    ternary_op_fn()
    list_declaration_fn()
    list_operations_fn()
    built_in_list_fn()
    built_in_set_fn()
    built_in_dict_fn()
    set_operations_fn()
    dict_operations_fn()
    default_dict_operations_fn()
    default_dict_methods_fn()
    default_dict_create_with_defaults()
    pass_by_value_test_fn()
    reassigning_a_ref_fn()
    pass_fn()
    interface_with_dataclasses_fn()
    number_conversions_fn()
    augment_operations_fn()
    empty_return_fn()
    test_all_exceptions_fn()
    shutil_exceptions_fn()
    print(A, B, C, D, E, a, b)
    dict_looping_fn()
    pure_lib_test_0_fn()

    perlin_noise_fn()
