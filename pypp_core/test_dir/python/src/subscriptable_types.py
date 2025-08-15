from pypp_bridge_library_test_0.subscriptable_type import (
    PseudoSubscriptableType,
    PseudoSubscriptableType2,
)


def subscriptable_types_fn():
    print("PYPP SUBSCRIPTABLE TYPES RESULTS:")
    a: PseudoSubscriptableType[int] = PseudoSubscriptableType[int](9)
    a.print()
    b: PseudoSubscriptableType[str] = PseudoSubscriptableType[str](10)
    b.print()
    c: PseudoSubscriptableType2[int] = PseudoSubscriptableType2[int]([1, 2])
    c.print()
    d: PseudoSubscriptableType2[str] = PseudoSubscriptableType2[str](["a", "b"])
    d.print()
    # Showing that you don't need the second '[str]' because of the C++ deduction guide
    #  for PseudoSubscriptableType2 that is in the bridge library.
    e: PseudoSubscriptableType2[str] = PseudoSubscriptableType2(["c", "d"])
    e.print()
