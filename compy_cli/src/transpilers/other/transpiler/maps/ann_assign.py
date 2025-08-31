from compy_cli.src.transpilers.other.transpiler.d_types import PySpecificImpFrom
from compy_cli.src.transpilers.other.transpiler.maps.d_types import (
    CustomMappingStartsWithEntry,
    AnnAssignsMap,
)


def _uni(
    type_cpp: str, target_str: str, _value_str: str, value_str_stripped: str
) -> str:
    if value_str_stripped == "std::monostate":
        value_str_stripped += "{}"
    return f"{type_cpp} {target_str}({value_str_stripped})"


ANN_ASSIGN_MAP: AnnAssignsMap = {
    "Uni<": {
        PySpecificImpFrom("compy_python.union", "Uni"): CustomMappingStartsWithEntry(
            _uni, []
        )
    },
}
