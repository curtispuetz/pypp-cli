SUBSCRIPT_VALUE_SQ_BRACKETS: set[str] = {
    "PyStr",
    "PyList",
    "PyDict",
    "PyTup",
    "PySet",
    "PyDefaultDict",
    "Uni",
}


# TODO: for bridge library creation, you let users specify types that should convert []
#  to <>.
def lookup_cpp_subscript_value_type(cpp_value: str) -> tuple[str, str]:
    if cpp_value in SUBSCRIPT_VALUE_SQ_BRACKETS:
        return cpp_value + "<", ">"
    return cpp_value + "[", "]"
