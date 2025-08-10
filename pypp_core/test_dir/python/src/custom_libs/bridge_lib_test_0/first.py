from dataclasses import dataclass

from pypp_bridge_library_test_0.pseudo_custom_type import PseudoCustomType
from pypp_python.configclass import configclass
from pypp_bridge_library_test_0 import test_namespace


def _as_arg(arg: PseudoCustomType):
    print(arg.get_a())


def _factory() -> PseudoCustomType:
    return PseudoCustomType(100)


class _ClassA:
    def __init__(self, pseudo_custom_type: PseudoCustomType):
        self._pseudo_custom_type = pseudo_custom_type

    def get_a(self) -> int:
        return self._pseudo_custom_type.get_a()


@dataclass(frozen=True, slots=True)
class _DataClassA:
    pseudo_custom_type: PseudoCustomType


@configclass
class _ConfigClassA:
    pseudo_custom_type: PseudoCustomType = PseudoCustomType(1)


def bridge_lib_test_0_fn():
    print("PYPP BRIDGE LIB TEST 0 RESULTS:")
    a: PseudoCustomType = PseudoCustomType(42)
    b: int = a.get_a()
    print(b)
    _as_arg(a)
    c: _ClassA = _ClassA(a)
    print(c.get_a())
    d: PseudoCustomType = _factory()
    print(d.get_a())
    e: _DataClassA = _DataClassA(a)
    print(e.pseudo_custom_type.get_a())
    print(_ConfigClassA.pseudo_custom_type.get_a())
    f: test_namespace.PseudoA = test_namespace.PseudoA(7)
    print(f.get_a())
