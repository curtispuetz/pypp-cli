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
    list_fn()
    set_fn()
    dict_fn()
    for_loop_fn()
