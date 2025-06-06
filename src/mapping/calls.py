from src.d_types import CppInclude, SBInc

CALL_MAP: dict[str, tuple[str, str, list[CppInclude]]] = {
    "print": ("std::cout << ", " << std:: endl;", [SBInc("iostream")])
}


def lookup_cpp_call(python_call: str, ret_imports: set[CppInclude]) -> tuple[str, str]:
    if python_call not in CALL_MAP:
        return python_call + "(", ")"
    val = CALL_MAP[python_call]
    for include in val[2]:
        ret_imports.add(include)
    return val[0], val[1]
