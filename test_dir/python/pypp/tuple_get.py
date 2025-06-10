from typing import TypeVar

T = TypeVar("T")


def pypp_tg(tup: tuple[any, ...], index: int) -> any:
    return tup[index]
