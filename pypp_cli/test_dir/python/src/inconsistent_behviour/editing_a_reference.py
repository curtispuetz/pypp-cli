def editing_a_reference_fn():
    print("INCONSISTENT BEHAVIOR RESULTS:")
    # Here is inconsistent behavior between Python and C++. For, now the solution is to
    # not do this. Why would you want to create a reference to an object when you
    # already have that object in your scope!?
    a: list[int] = [1, 2, 3]
    b: list[int] = a
    b.append(4)
    # prints [1, 2, 3, 4] in Python, but [1, 2, 3] in C++
    print(f"inconsistent behavior: {a}")

    # Here is another example of pretty much the same thing, (and again, its
    # inconsistent behavior). Here, you can just use c still. You don't need d.
    c: list[int] = [1, 2, 3]
    d: list[int] = update_and_return_new(c)
    d[3] = 99
    print(f"inconsistent behavior: {c}")


def update_and_return_new(l1: list[int]) -> list[int]:
    # This should return-by-reference
    l1.append(4)
    return l1
