from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    NameMap,
    ToStringEntry,
)


EXCEPTION_NAME_MAP: NameMap = {
    "Exception": {
        None: ToStringEntry("pypp::Exception", [QInc("exceptions/exception.h")])
    },
    "ValueError": {
        None: ToStringEntry("pypp::ValueError", [QInc("exceptions/stdexcept.h")])
    },
    "TypeError": {
        None: ToStringEntry("pypp::TypeError", [QInc("exceptions/stdexcept.h")])
    },
    "KeyError": {
        None: ToStringEntry("pypp::KeyError", [QInc("exceptions/stdexcept.h")])
    },
    "IndexError": {
        None: ToStringEntry("pypp::IndexError", [QInc("exceptions/stdexcept.h")])
    },
    "NotImplementedError": {
        None: ToStringEntry(
            "pypp::NotImplementedError", [QInc("exceptions/stdexcept.h")]
        )
    },
    "AttributeError": {
        None: ToStringEntry("pypp::AttributeError", [QInc("exceptions/stdexcept.h")])
    },
    "ZeroDivisionError": {
        None: ToStringEntry("pypp::ZeroDivisionError", [QInc("exceptions/stdexcept.h")])
    },
    "OSError": {
        None: ToStringEntry("pypp::OSError", [QInc("exceptions/system_error.h")])
    },
    "FileNotFoundError": {
        None: ToStringEntry(
            "pypp::FileNotFoundError", [QInc("exceptions/filesystem.h")]
        )
    },
    "IOError": {None: ToStringEntry("pypp::IOError", [QInc("exceptions/ios.h")])},
    "MemoryError": {
        None: ToStringEntry("pypp::MemoryError", [QInc("exceptions/new.h")])
    },
    "NameError": {
        None: ToStringEntry("pypp::NameError", [QInc("exceptions/exception.h")])
    },
    "ImportError": {
        None: ToStringEntry("pypp::ImportError", [QInc("exceptions/exception.h")])
    },
    "StopIteration": {
        None: ToStringEntry("pypp::StopIteration", [QInc("exceptions/exception.h")])
    },
    "RuntimeError": {
        None: ToStringEntry("pypp::RuntimeError", [QInc("exceptions/stdexcept.h")])
    },
    "AssertionError": {
        None: ToStringEntry("pypp::AssertionError", [QInc("exceptions/stdexcept.h")])
    },
    "SystemError": {
        None: ToStringEntry("pypp::SystemError", [QInc("exceptions/system_error.h")])
    },
}
