from test_dir.python.pypp.custom_types import PyppMut


def list_as_arg(a: list[int]):
    b: list[int] = a * 2
    print(b)


def list_as_mutable_arg(a: PyppMut(list[int])):
    a *= 3
    print(a)
