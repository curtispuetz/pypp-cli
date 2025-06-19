from test_dir.python.pypp.custom_types import PyppMut


def editing_a_reference_fn():
    # Here is inconsistent behavior between Python and C++. For, now the solution is to
    # not do this. Why would you want to create a reference to an object when you
    # already have that object in your scope!?
    a: list[int] = [1, 2, 3]
    b: list[int] = a
    b.append(4)
    print(a)  # prints [1, 2, 3, 4] in Python, but [1, 2, 3] in C++

    # Here is another example of pretty much the same thing, (and again, its
    # inconsistent behavior). Here, you can just use c still. You don't need d.
    # However, imagine if we didn't pass c in here and instead we called like a method
    # and we wanted that one to append to some list and return the list? In this case,
    # would we want to return the reference? We could, but its not going to be supported
    # in pypp. Instead, that object that we want to reference should be injected here
    # everywhere that we need it. So, we would editing the list by calling that function
    # and we wouldn't need to return the list because we should already have that
    # objects reference here.
    c: list[int] = [1, 2, 3]
    d: list[int] = update_and_return_new(c)
    d[-1] = 99
    print(c)


def update_and_return_new(l1: PyppMut(list[int])) -> list[int]:
    l1.append(4)
    return l1