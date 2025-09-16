from dataclasses import dataclass

from pypp_bridge_library_test_0.pseudo_custom_type import PseudoCustomType
from pypp_python import configclass, Ref
from pypp_bridge_library_test_0 import test_namespace
from pypp_bridge_library_test_0.name_only_call import name_only_call_fn
from pypp_bridge_library_test_0.include_only_call import include_only_call_fn
from pypp_bridge_library_test_0.custom_mapping_call import tg_plus_one
from pypp_bridge_library_test_0.custom_mapping_starts_with_call import PseudoGeneric
from pypp_bridge_library_test_0.modules_to_cpp_inc import pseudo_fn_a
import pypp_bridge_library_test_0.modules_to_cpp_inc_2 as m2
import pypp_bridge_library_test_0.replace_with_double_colon_call as dc_test
from pypp_bridge_library_test_0.custom_print import custom_print
from pypp_bridge_library_test_0.custom_list import PseudoCustomList


def _as_arg(arg: PseudoCustomType):
    print(arg.get_a())


def _factory() -> PseudoCustomType:
    return PseudoCustomType(100)


@dataclass(frozen=True, slots=True)
class _ClassA:
    _pseudo_custom_type: PseudoCustomType

    def get_a(self) -> int:
        return self._pseudo_custom_type.get_a()


@configclass
class _ConfigClassA:
    pseudo_custom_type: PseudoCustomType = PseudoCustomType(1)


def bridge_lib_test_0_fn():
    print("pypp BRIDGE LIB TEST 0 RESULTS:")
    a: PseudoCustomType = PseudoCustomType(42)
    b: int = a.get_a()
    print(b)
    _as_arg(a)
    c: _ClassA = _ClassA(a)
    print(c.get_a())
    d: PseudoCustomType = _factory()
    print(d.get_a())
    print(_ConfigClassA.pseudo_custom_type.get_a())
    f: test_namespace.PseudoA = test_namespace.PseudoA(7)
    print(f.get_a())
    print(name_only_call_fn())
    print(include_only_call_fn())
    g: tuple[int, int] = (1, 2)
    print(tg_plus_one(g, 0))
    h: PseudoGeneric[int] = PseudoGeneric[int](3)
    h.print_value()
    i: PseudoGeneric[str] = PseudoGeneric[str](str)  # type: ignore
    i.print_value()
    j: int = dc_test.sub_namespace.test_fn()
    print(j)
    print(pseudo_fn_a())
    print(m2.pseudo_fn_b())
    custom_print("aloha")
    k: PseudoCustomList[int] = PseudoCustomList([1, 2, 3])
    print(Ref(k))
