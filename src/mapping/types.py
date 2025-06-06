from src.d_types import CppInclude, SBInc

TYPES_MAP: dict[str, tuple[str, list[CppInclude]]] = {
    "str": ("std::string", [SBInc("string")]),
    "int": ("int", []),
}


def lookup_cpp_type(python_type: str, ret_imports: set[CppInclude]) -> str:
    # The way it works is that whenever you looked up the type, it automatically
    # is added to the ret_imports
    if python_type not in TYPES_MAP:
        return python_type
    val = TYPES_MAP[python_type]
    for include in val[1]:
        ret_imports.add(include)
    return val[0]
