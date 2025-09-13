from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    NameMap,
    ToStringEntry,
)


# TODO now: got to delete some of these
EXCEPTION_NAME_MAP: NameMap = {
    "Exception": {
        None: ToStringEntry("pypp::Exception", [QInc("exceptions/exception.h")])
    },
    "ValueError": {
        None: ToStringEntry("pypp::ValueError", [QInc("exceptions/common.h")])
    },
    "KeyError": {None: ToStringEntry("pypp::KeyError", [QInc("exceptions/common.h")])},
    "IndexError": {
        None: ToStringEntry("pypp::IndexError", [QInc("exceptions/common.h")])
    },
    "NotImplementedError": {
        None: ToStringEntry("pypp::NotImplementedError", [QInc("exceptions/common.h")])
    },
    "RuntimeError": {
        None: ToStringEntry("pypp::RuntimeError", [QInc("exceptions/common.h")])
    },
    "AssertionError": {
        None: ToStringEntry("pypp::AssertionError", [QInc("exceptions/common.h")])
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
