from pypp_cli.do.transpile.transpile.z_i.d_types import QInc
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import (
    NameMap,
    ToStringEntry,
)


EXCEPTION_NAME_MAP: NameMap = {
    "Exception": {
        None: ToStringEntry("pypp::Exception", [QInc("exceptions/exception.h")])
    },
    "ValueError": {
        None: ToStringEntry("pypp::ValueError", [QInc("exceptions/common.h")])
    },
    "AssertionError": {
        None: ToStringEntry("pypp::AssertionError", [QInc("exceptions/common.h")])
    },
    "LookupError": {
        None: ToStringEntry("pypp::LookupError", [QInc("exceptions/common.h")])
    },
    "IndexError": {
        None: ToStringEntry("pypp::IndexError", [QInc("exceptions/common.h")])
    },
    "KeyError": {None: ToStringEntry("pypp::KeyError", [QInc("exceptions/common.h")])},
    "RuntimeError": {
        None: ToStringEntry("pypp::RuntimeError", [QInc("exceptions/common.h")])
    },
    "NotImplementedError": {
        None: ToStringEntry("pypp::NotImplementedError", [QInc("exceptions/common.h")])
    },
    "OSError": {
        None: ToStringEntry("pypp::OSError", [QInc("exceptions/filesystem.h")])
    },
    "FileNotFoundError": {
        None: ToStringEntry(
            "pypp::FileNotFoundError", [QInc("exceptions/filesystem.h")]
        )
    },
    "NotADirectoryError": {
        None: ToStringEntry(
            "pypp::NotADirectoryError", [QInc("exceptions/filesystem.h")]
        )
    },
    "PermissionError": {
        None: ToStringEntry("pypp::PermissionError", [QInc("exceptions/filesystem.h")])
    },
    "FileExistsError": {
        None: ToStringEntry("pypp::FileExistsError", [QInc("exceptions/filesystem.h")])
    },
}
