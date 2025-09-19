def list_as_arg(a: list[int]):
    b: list[int] = a * 2
    print(b)


def list_as_mutable_arg(a: list[int]):
    a *= 3
    print(a)
