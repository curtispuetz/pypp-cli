from pypp_python import (
    float32,
    to_float32,
    int8_t,
    int16_t,
    int32_t,
    int64_t,
    uint8_t,
    uint16_t,
    uint32_t,
    uint64_t,
    to_int8_t,
    to_int16_t,
    to_int32_t,
    to_int64_t,
    to_uint8_t,
    to_uint16_t,
    to_uint32_t,
    to_uint64_t,
)


def number_conversions_fn():
    print("NUMBER CONVERSIONS RESULTS:")
    a: str = "123"
    b: str = "45.67"

    # converting str to numbers
    a_int: int = int(a)
    b_float: float = float(b)
    b_float32: float32 = to_float32(b_float)
    a_bool: bool = bool(a_int)  # should be True since a_int is 123
    print(
        f"int(a): {a_int}, float(b): {b_float}, "
        f"float32(b): {b_float32}, bool(a): {a_bool}"
    )

    # converting numbers of different types
    a_float: float = float(a_int)
    a_float32: float32 = to_float32(a_float)
    b_int: int = int(b_float)
    b_bool: bool = bool(b_float)
    print(
        f"float(a): {a_float}, float32(a): {a_float32}, int(b): {b_int}, "
        f"bool(b): {b_bool}"
    )

    # converting cstdint numbers of different types
    a_int8_t: int8_t = to_int8_t(257)  # This is too large for int8_t. Goes to like 1
    a_int16_t: int16_t = to_int16_t(a_int)
    a_int32_t: int32_t = to_int32_t(a_int)
    a_int64_t: int64_t = to_int64_t(a_int)
    a_uint8_t: uint8_t = to_uint8_t(a_int)
    a_uint16_t: uint16_t = to_uint16_t(a_int)
    a_uint32_t: uint32_t = to_uint32_t(a_int)
    a_uint64_t: uint64_t = to_uint64_t(a_int)
    print(
        f"int8_t: {a_int8_t}, int16_t: {a_int16_t}, int32_t: {a_int32_t}, "
        f"int64_t: {a_int64_t}, uint8_t: {a_uint8_t}, uint16_t: {a_uint16_t}, "
        f"uint32_t: {a_uint32_t}, uint64_t: {a_uint64_t}"
    )
