from typing import TypeVar, Any

T = TypeVar("T")


def pypp_dg(d: dict[Any, T], index: int) -> T:
    # note: Use pypp_dg to access dictionary elements instead of dict[index].
    # dict[index] can still be used, but at your own risk, because if the index does
    # not exist in the dict, in the C++ transpiled code a KeyError won't be raised, and
    # undefined behaviour will happen. Using pypp_dg instead will result in the same
    # behavior in the C++ build, since a KeyError will the thrown.
    # tldr; dict[index] can be used if you know index is in the dict. If it isn't in the
    # dict, C++ will have undefined behavior.
    return d[index]
