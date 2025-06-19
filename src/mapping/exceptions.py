from src.d_types import QInc
from src.util.ret_imports import RetImports, add_inc

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


def lookup_cpp_exception_type(python_type: str, ret_imports: RetImports) -> str:
    if python_type not in PY_TO_CPP_INCLUDE_MAP:
        raise Exception(f"unsupported exception type: {python_type}")
    add_inc(ret_imports, PY_TO_CPP_INCLUDE_MAP[python_type])
    return "Pypp" + python_type
