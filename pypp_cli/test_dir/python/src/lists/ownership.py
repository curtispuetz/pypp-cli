from dataclasses import dataclass
from pypp_python import print_address, mov


@dataclass
class _PrivateClass:
    _v: int

    def m(self) -> int:
        return self._v


def _calc_list() -> list[str]:
    a: str = "a"
    # List created like this uses C++ initializer lists and I think always copies the
    # values, which is fine.
    return [a, "b", "c"]


def _calc_obj_list() -> list[_PrivateClass]:
    a: _PrivateClass = _PrivateClass(1)
    return [a, _PrivateClass(2), _PrivateClass(3)]


def list_ownership_tests_fn():
    print("LIST OWNERSHIP TESTS RESULTS:")
    a: list[str] = _calc_list()
    print(a)
    b: str = "d"
    a.append(mov(b))
    print(a)
    c: list[_PrivateClass] = _calc_obj_list()
    print_address(c)
