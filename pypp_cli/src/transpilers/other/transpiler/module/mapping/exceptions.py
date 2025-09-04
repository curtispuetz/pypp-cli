from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps

PY_TO_CPP_INCLUDE_MAP: dict[str, QInc] = {
    "Exception": QInc("exceptions/exception.h"),
    "NameError": QInc("exceptions/exception.h"),
    "ImportError": QInc("exceptions/exception.h"),
    "StopIteration": QInc("exceptions/exception.h"),
    "RuntimeError": QInc("exceptions/stdexcept.h"),
    "ValueError": QInc("exceptions/stdexcept.h"),
    "TypeError": QInc("exceptions/stdexcept.h"),
    "IndexError": QInc("exceptions/stdexcept.h"),
    "KeyError": QInc("exceptions/stdexcept.h"),
    "AssertionError": QInc("exceptions/stdexcept.h"),
    "NotImplementedError": QInc("exceptions/stdexcept.h"),
    "AttributeError": QInc("exceptions/stdexcept.h"),
    "ZeroDivisionError": QInc("exceptions/stdexcept.h"),
    "OSError": QInc("exceptions/system_error.h"),
    "SystemError": QInc("exceptions/system_error.h"),
    "FileNotFoundError": QInc("exceptions/filesystem.h"),
    "IOError": QInc("exceptions/ios.h"),
    "MemoryError": QInc("exceptions/new.h"),
}


def lookup_cpp_exception_type(exception: str, d: Deps) -> str:
    if exception not in PY_TO_CPP_INCLUDE_MAP:
        return exception
    d.add_inc(PY_TO_CPP_INCLUDE_MAP[exception])
    return "Pypp" + exception
