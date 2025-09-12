from args_test import args_test_fn
from augment_operations import augment_operations_fn
from built_in_functions.dict_fn import built_in_dict_fn
from built_in_functions.list_fn import built_in_list_fn
from built_in_functions.number_conversions import number_conversions_fn
from built_in_functions.set_fn import built_in_set_fn
from custom_libs.bridge_lib_test_0.first import bridge_lib_test_0_fn
from custom_libs.bridge_lib_test_1.first import bridge_lib_test_1_fn
from dataclasses_test.nested_dependencies import dataclass_nested_dependencies_fn
from default_dict.create_with_defaults import default_dict_create_with_defaults
from default_dict.methods import default_dict_methods_fn
from default_dict.operations import default_dict_operations_fn
from dicts.operations import dict_operations_fn
from empty_return import empty_return_fn
from exceptions.custom_exceptions import custom_exception_fn
from file_io.test_is_here import test_is_here_fn
from first import return_something
from imports_test.first import imports_test_fn
from imports_test.second import imports_test_fn2
from inconsistent_behviour.reassigning_a_ref import reassigning_a_ref_fn
from interfaces.with_dataclasses import interface_with_dataclasses_fn
from lambdas import lambdas_fn
from lists.ownership import list_ownership_tests_fn
from number_types.in_collections import number_types_in_collections_fn
from pass_by_value import pass_by_value_test_fn
from random_library.first import random_fn
from second import return_friend
from sets.operations import set_operations_fn
from subscriptable_types import subscriptable_types_fn
from third import using_inline_string
from fourth import string_as_argument
from if_elif_else.if_elif_else import if_elif_else_fn
from lists.lists import list_fn
from strings.first import string_ops
from numbers_test.first import number_ops
from lists.as_arg import list_as_arg, list_as_mutable_arg
from dicts.first import dict_fn
from tuples.first import tuples_fn
from sets.first import set_fn
from loops.for_ import for_loop_fn
from loops.while_ import while_loop_fn
from exceptions.throw_ import throw_fn
from dicts.exceptions import dict_exceptions_fn
from lists.exceptions import list_exceptions_fn
from sets.exceptions import set_exceptions_fn
from strings.exceptions import string_exceptions_fn
from tuples.exceptions import tuple_exceptions_fn
from file_io.first import file_io_fn
from strings.special_characters import string_esc_chars_fn
from strings.f_strings import f_strings_fn
from ranges.first import ranges_fn
from slices.first import slices_fn
from inconsistent_behviour.editing_a_reference import editing_a_reference_fn
from loops.enumerate_ import enumerate_fn
from printing.first import printing_fn
from loops.zip_ import zip_fn
from loops.reversed_ import reversed_fn
from lists.comprehensions import list_comprehension_fn
from sets.comprehensions import set_comprehension_fn
from dicts.comprehensions import dict_comprehension_fn
from exceptions.assert_ import assert_fn
from type_aliases import type_aliases_fn
from yields.first import yield_fn
from math_library.first import math_library_fn
from time_library.first import time_library_fn
from sets.of_tuples import set_of_tuples_fn
from ref_vars import ref_vars_fn
from dataclasses_test.first import dataclass_fn
from dataclasses_test.with_methods import dataclass_with_methods_fn
from interfaces.first import interfaces_fn
from operations import operations_fn
from fn_as_vars.first import fn_as_vars_fn
from default_dict.first import default_dict_fn
from pypp_union.first import pypp_union_fn
from constants import constant_fn
from number_types.number_types import number_types_fn
from triple_quote_strings import triple_quote_strings_fn
from ternary_op import ternary_op_fn
from lists.declaration import list_declaration_fn
from lists.operations import list_operations_fn
from using_pass import pass_fn


if __name__ == "__main__":
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
