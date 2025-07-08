from typing import TypeVar

T = TypeVar("T")


def print_address(_type: T):
    print(hex(id(_type)))
