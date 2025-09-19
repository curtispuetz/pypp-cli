from pypp_python import Valu, mov, dataclass


@dataclass(frozen=True, slots=True)
class MyType:
    field1: Valu(str)
    field2: Valu(list[int])


def my_type_factory(a: Valu(list[int])) -> MyType:
    return MyType("first arg", mov(a))


def pass_by_value_test_fn():
    print("PASS BY VALUE RESULTS:")
    # example 1 with temporary
    b: MyType = my_type_factory([1, 2, 3])
    print(b.field2)
    # example 2 with mov
    c: list[int] = [4, 5, 6]
    d: MyType = my_type_factory(mov(c))
    # c is a valid state but unspecified after mov. So just like C++, shouldn't be used.
    print(d.field2)
    # example 3 with copy (Recommended not to do this)
    e: list[int] = [7, 8, 9]
    f: MyType = my_type_factory(e)
    e.append(10)
    # Should print [7, 8, 9] in C++ since a copy was made, but [7, 8, 9, 10] in Python
    # since lists are passed by reference.
    print(f"{f.field2} (should be [7, 8, 9] with C++)")
    # Therefore, the rule-of-thumb is to only pass temporaries or use mov() when passing
    # to a function that takes a pass-by-value argument.

    # If you want something like example 3 you can do:
    g: list[int] = [11, 12, 13]
    i: MyType = my_type_factory(g.copy())  # do an explicit copy
    g.append(-1)
    print(i.field2)
