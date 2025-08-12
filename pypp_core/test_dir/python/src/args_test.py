from pypp_python.custom_types import (
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
