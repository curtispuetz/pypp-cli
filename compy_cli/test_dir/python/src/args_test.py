from compy_python import (
    float32,
    int8_t,
    int16_t,
    int32_t,
    int64_t,
    uint8_t,
    uint16_t,
    uint32_t,
    uint64_t,
)

from compy_bridge_library_test_0.pass_by_value_test import pseudo_int8_t, pseudo_int16_t


def int_arg(a: int):
    print(a)


def float_arg(a: float):
    print(a)


# only one that should be pass-by-reference
def str_arg(a: str):
    print(a)


def bool_arg(a: bool):
    print(a)


def float32_arg(a: float32):
    print(a)


def int8_t_arg(a: int8_t):
    print(a)


def int16_t_arg(a: int16_t):
    print(a)


def int32_t_arg(a: int32_t):
    print(a)


def int64_t_arg(a: int64_t):
    print(a)


def uint8_t_arg(a: uint8_t):
    print(a)


def uint16_t_arg(a: uint16_t):
    print(a)


def uint32_t_arg(a: uint32_t):
    print(a)


def uint64_t_arg(a: uint64_t):
    print(a)


# This one is from a bridge library
def pseudo_int8_t_arg(a: pseudo_int8_t):
    print(a)


# This one is from a bridge library
def pseudo_int16_t_arg(a: pseudo_int16_t):
    print(a)


def args_test_fn():
    print("compy ARGS TEST RESULTS:")
    a: int = 42
    int_arg(a)
    b: float = 3.14
    float_arg(b)
    c: str = "Hello, World!"
    str_arg(c)
    d: bool = True
    bool_arg(d)
    e: float32 = 1.23
    float32_arg(e)
    f: int8_t = 8
    int8_t_arg(f)
    g: int16_t = 16
    int16_t_arg(g)
    h: int32_t = 32
    int32_t_arg(h)
    i: int64_t = 64
    int64_t_arg(i)
    j: uint8_t = 8
    uint8_t_arg(j)
    k: uint16_t = 16
    uint16_t_arg(k)
    l: uint32_t = 32
    uint32_t_arg(l)
    m: uint64_t = 64
    uint64_t_arg(m)
    n: pseudo_int8_t = 8
    pseudo_int8_t_arg(n)
    o: pseudo_int16_t = 16
    pseudo_int16_t_arg(o)
