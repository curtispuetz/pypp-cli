from pypp_core.src.d_types import CppInclude, PySpecificImport
from pypp_core.src.deps import Deps


import ast
from dataclasses import dataclass, field
from typing import Callable


@dataclass(frozen=True, slots=True)
class CallsTranspile:
    imp: PySpecificImport
    caller_str: str
    fn: Callable[[ast.Call, Deps], str] | None = field(default=None)
    fn_starts_with: Callable[[ast.Call, Deps, str], str] | None = field(default=None)
    replace_dot_with_double_colon_include: CppInclude | None = field(default=None)

    def __post_init__(self):
        non_none_count = sum(
            x is not None
            for x in (
                self.fn,
                self.fn_starts_with,
                self.replace_dot_with_double_colon_include,
            )
        )
        if non_none_count != 1:
            raise ValueError(
                "One and only one of 'fn', 'fn_starts_with', and "
                "'replace_dot_with_double_colon_include' must be non-None."
            )
