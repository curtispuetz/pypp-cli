NP_TYPE_TO_CPP_TYPE: dict[str, str] = {
    # Integer types
    # "np.int8": "int8_t",  # Not supported because the printing was weird and I don't care about these
    # "np.uint8": "uint8_t",  # ^
    "np.int16": "int16_t",
    "np.uint16": "uint16_t",
    "np.int32": "int32_t",
    "np.uint32": "uint32_t",
    "np.int64": "int64_t",
    "np.uint64": "uint64_t",
    # "np.int_": "int", # not supported platform default (usually int32 or int64)
    "np.uint": "unsigned int",  # platform default unsigned
    # Floating-point types
    # "np.float16": " not supported /* no native C++ equivalent */",
    "np.float32": "float",
    "np.float64": "double",
    # "np.float_": "double",  # not supported alias for float64
    "np.longdouble": "long double",
    # Complex types (not supported)
    # "np.complex64": "std::complex<float>",
    # "np.complex128": "std::complex<double>",
    # "np.complex_": "std::complex<double>",
    # Boolean
    "np.bool": "bool",
    # "np.bool_": "bool",  # not supported (just use np.bool).
    # not supported String / Object types
    # "np.str_": "std::wstring",  # or custom type if needed
    # "np.bytes_": "std::string",
    # "np.object_": "void*",  # or custom wrapper for Python object
}
