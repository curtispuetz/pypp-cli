from pypp_python import Ref


def _get_list(input_list: list[int]) -> Ref(list[int]):
    return input_list


def repeat(a: list[int]) -> Ref(list[int]):
    a *= 2
    return a


def repeat_new(a: list[int]) -> list[int]:
    return a * 2


def ref_vars_fn():
    print("REF VARS RESULTS:")
    a: list[list[int]] = [[1, 2], [3, 4]]
    print(a)
    # copy
    b: list[int] = a[0]
    b.append(5)
    print("Python and C++ should print different results:")
    print(a)
    # reference
    c: list[list[int]] = [[1, 2], [3, 4]]
    d: Ref(list[int]) = c[0]
    d.append(5)
    print("Python and C++ should print the same results:")
    print(c)
    # with dicts
    e: dict[int, list[int]] = {0: [1, 2], 1: [3, 4]}
    f: Ref(list[int]) = e[0]
    f.append(5)
    print(e)
    # a function that returns a reference
    original_list: list[int] = [1, 2, 3]
    g: Ref(list[int]) = _get_list(original_list)
    g.append(4)
    print(original_list)

    # repeat
    arr2: list[int] = [1, 2]
    arr2_ref: Ref(list[int]) = repeat(arr2)
    arr2_ref.append(42)
    print(arr2)  # should print [1, 2, 1, 2, 42]
    # recommended to not do this.
    arr3: list[int] = [1, 2]
    arr_3_copy: list[int] = repeat(arr3)
    arr_3_copy.append(42)
    # should print [1, 2, 1, 2] in C++, but [1, 2, 1, 2, 42] in Python!
    print(arr3)

    # repeat new
    arr4: list[int] = [1, 2]
    arr4_copy: list[int] = repeat_new(arr4)
    arr4_copy.append(42)
    print(arr4)  # should print [1, 2] for both C++ and Python

    # just a reference to a list
    arr5: list[int] = [1, 2]
    arr5_ref: Ref(list[int]) = arr5
    arr5_ref.append(42)
    print(arr5)  # should print [1, 2, 42] for both C++ and Python
