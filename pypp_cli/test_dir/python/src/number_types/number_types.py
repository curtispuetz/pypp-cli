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


def number_types_fn():
    print("NUMBER TYPES RESULTS:")
    a: int8_t = -1
    b: int16_t = -129
    c: int32_t = -32769
    d: int64_t = -2147483649
    e: uint8_t = 1
    f: uint16_t = 256
    g: uint32_t = 65536
    h: uint64_t = 4294967296
    print(a, b, c, d, e, f, g, h)
    i: float32 = 3.14
    print(i)
