from pypp_core.src.d_types import PySpecificImport, PySpecificImpFrom
from pypp_core.src.deps import Deps

SUBSCRIPT_VALUE_SQ_BRACKETS: dict[str, PySpecificImport | None] = {
    "PyStr": None,
    "PyList": None,
    "PyDict": None,
    "PyTup": None,
    "PySet": None,
    "PyDefaultDict": PySpecificImpFrom("collections", "defaultdict"),
    "Uni": PySpecificImpFrom("pypp_python.union", "Uni"),
}


# TODO: for bridge library creation, you let users specify types that should convert []
#  to <>.
def lookup_cpp_subscript_value_type(cpp_value: str, d: Deps) -> tuple[str, str]:
    if cpp_value in SUBSCRIPT_VALUE_SQ_BRACKETS:
        r = SUBSCRIPT_VALUE_SQ_BRACKETS[cpp_value]
        if r is None or d.is_imported(r):
            return cpp_value + "<", ">"
    return cpp_value + "[", "]"
