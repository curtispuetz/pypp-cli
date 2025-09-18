from pypp_cli.src.transpilers.library.bridge_libs.models import (
    CustomMappingValueModel,
    LeftAndRightValueModel,
    ReplaceDotWithDoubleColonValueModel,
    ToStringValueModel,
)
from pypp_cli.src.transpilers.library.transpiler.maps.d_types import (
    CustomMappingFromLibEntry,
    CustomMappingStartsWithFromLibEntry,
    LeftAndRightEntry,
    ReplaceDotWithDoubleColonEntry,
    ToStringEntry,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.util import (
    calc_cpp_include,
)


# TODO: move this to somewhere that makes more sense.


def calc_to_string_entry(d: ToStringValueModel) -> ToStringEntry:
    return ToStringEntry(d.to, calc_cpp_include(d.quote_includes, d.angle_includes))


def calc_custom_mapping_from_lib_entry(
    d: CustomMappingValueModel,
) -> CustomMappingFromLibEntry:
    return CustomMappingFromLibEntry(
        "\n".join(d.mapping_function),
        calc_cpp_include(d.quote_includes, d.angle_includes),
    )


def calc_custom_mapping_starts_with_from_lib_entry(
    d: CustomMappingValueModel,
) -> CustomMappingStartsWithFromLibEntry:
    return CustomMappingStartsWithFromLibEntry(
        "\n".join(d.mapping_function),
        calc_cpp_include(d.quote_includes, d.angle_includes),
    )


def calc_replace_dot_with_double_colon_entry(
    d: ReplaceDotWithDoubleColonValueModel,
) -> ReplaceDotWithDoubleColonEntry:
    return ReplaceDotWithDoubleColonEntry(
        calc_cpp_include(d.quote_includes, d.angle_includes), False
    )


def calc_left_and_right_entry(obj: LeftAndRightValueModel) -> LeftAndRightEntry:
    return LeftAndRightEntry(
        obj.left, obj.right, calc_cpp_include(obj.quote_includes, obj.angle_includes)
    )
