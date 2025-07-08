from src.first import return_something
from src.second import return_friend
from src.third import using_inline_string
from src.fourth import string_as_argument
from src.if_elif_else.if_elif_else import if_elif_else_fn
from src.lists.lists import list_fn
from src.strings.first import string_ops
from src.numbers.first import number_ops
from src.lists.as_arg import list_as_arg, list_as_mutable_arg
from src.dicts.first import dict_fn
from src.tuples.first import tuples_fn
from src.sets.first import set_fn
from src.loops.for_ import for_loop_fn
from src.loops.while_ import while_loop_fn
from src.excpetions.throw_ import throw_fn
from src.dicts.exceptions import dict_exceptions_fn
from src.lists.exceptions import list_exceptions_fn
from src.sets.exceptions import set_exceptions_fn
from src.strings.exceptions import string_exceptions_fn
from src.tuples.exceptions import tuple_exceptions_fn
from src.file_io.first import file_io_fn
from src.strings.escape_characters import string_esc_chars_fn
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
from src.excpetions.assert_ import assert_fn
from src.type_aliases import type_aliases_fn
from src.yields.first import yield_fn
from src.math_library.first import math_library_fn
from src.time_library.first import time_library_fn
from src.sets.of_tuples import set_of_tuples_fn
from src.ref_vars import ref_vars_fn
from src.dataclasses.first import dataclass_fn
from src.dataclasses.with_methods import dataclass_with_methods_fn
from src.classes.first import classes_fn
from src.classes.inheritance import class_inheritance_fn
from src.interfaces.first import interfaces_fn

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
    time_library_fn()
    tuples_fn()
    set_of_tuples_fn()
    ref_vars_fn()
    dict_fn()
    list_fn()
    dataclass_fn()
    dataclass_with_methods_fn()
    classes_fn()
    class_inheritance_fn()
    interfaces_fn()
