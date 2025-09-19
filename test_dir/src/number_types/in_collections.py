from pypp_python import (
    int8_t,
    int32_t,
    int64_t,
    int16_t,
    uint8_t,
    uint16_t,
    uint32_t,
    uint64_t,
    float32,
)


def _lists():
    a: list[int8_t] = [1, 2, 3, 4]
    print(a)
    b: list[int16_t] = [5, 6, 7, 8]
    print(b)
    c: list[int32_t] = [9, 10, 11, 12]
    print(c)
    d: list[int64_t] = [13, 14, 15, 16]
    print(d)
    e: list[uint8_t] = [17, 18, 19, 20]
    print(e)
    f: list[uint16_t] = [21, 22, 23, 24]
    print(f)
    g: list[uint32_t] = [25, 26, 27, 28]
    print(g)
    h: list[uint64_t] = [29, 30, 31, 32]
    print(h)
    i: list[float32] = [3.14, 2.71, 1.61]
    print(i)


def _sets():
    a: set[int8_t] = {1, 2, 3, 4}
    print(a)
    b: set[int16_t] = {5, 6, 7, 8}
    print(b)
    c: set[int32_t] = {9, 10, 11, 12}
    print(c)
    d: set[int64_t] = {13, 14, 15, 16}
    print(d)
    e: set[uint8_t] = {17, 18, 19, 20}
    print(e)
    f: set[uint16_t] = {21, 22, 23, 24}
    print(f)
    g: set[uint32_t] = {25, 26, 27, 28}
    print(g)
    h: set[uint64_t] = {29, 30, 31, 32}
    print(h)
    i: set[float32] = {3.14, 2.71, 1.61}
    print(i)


def _dicts():
    a: dict[int8_t, str] = {1: "a", 2: "b"}
    print(a)
    b: dict[int16_t, str] = {3: "c", 4: "d"}
    print(b)
    c: dict[int32_t, str] = {5: "e", 6: "f"}
    print(c)
    d: dict[int64_t, str] = {7: "g", 8: "h"}
    print(d)
    e: dict[uint8_t, str] = {9: "i", 10: "j"}
    print(e)
    f: dict[uint16_t, str] = {11: "k", 12: "l"}
    print(f)
    g: dict[uint32_t, str] = {13: "m", 14: "n"}
    print(g)
    h: dict[uint64_t, str] = {15: "o", 16: "p"}
    print(h)
    i: dict[float32, str] = {3.14: "q", 2.71: "r"}
    print(i)
    j: dict[int16_t, float32] = {1: 3.14, 2: 2.71}
    print(j)
    k: dict[uint16_t, int32_t] = {1: 1, 2: 2}
    print(k)


def _list_factory() -> list[uint16_t]:
    # Note: you have to explicitly create the variable and return it.
    #  You can't just do: return [1, 2, 3, 4]. Because the type can't be inferred
    #  properly by the C++ compiler.
    ret: list[uint16_t] = [1, 2, 3, 4]
    return ret


def _set_factory() -> set[uint16_t]:
    ret: set[uint16_t] = {1, 2, 3, 4}
    return ret


def _dict_factory() -> dict[uint16_t, str]:
    return {1: "a", 2: "b"}


def number_types_in_collections_fn():
    print("NUMBER TYPES IN COLLECTIONS RESULTS:")
    _lists()
    _sets()
    _dicts()
    print(_list_factory())
    print(_set_factory())
    print(_dict_factory())
