from pypp_cli.do.transpile.transpile.y.d_types import PySpecificImpFrom
from pypp_cli.do.transpile.transpile.y.maps.d_types import (
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
    "pypp::Uni<": {
        PySpecificImpFrom("pypp_python", "Uni"): CustomMappingStartsWithEntry(_uni, [])
    },
}
