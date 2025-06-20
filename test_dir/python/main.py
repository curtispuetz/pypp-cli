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
from src.numpy_arrays.first import numpy_arrays_fn
from src.loops.for_ import for_loop_fn
from src.loops.while_ import while_loop_fn
from src.excpetions.throw_ import throw_fn
from src.dicts.exceptions import dict_exceptions_fn
from src.lists.exceptions import list_exceptions_fn
from src.numpy_arrays.exceptions import numpy_array_exceptions_fn
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
    tuples_fn()
    string_ops()
    numpy_arrays_fn()
    set_fn()
    for_loop_fn()
    while_loop_fn()
    throw_fn()
    list_fn()
    dict_fn()
    dict_exceptions_fn()
    list_exceptions_fn()
    numpy_array_exceptions_fn()
    set_exceptions_fn()
    string_exceptions_fn()
    tuple_exceptions_fn()
    file_io_fn()
    string_esc_chars_fn()
    f_strings_fn()
    ranges_fn()
    slices_fn()
    editing_a_reference_fn()
    enumerate_fn()
