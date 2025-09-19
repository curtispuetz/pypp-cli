from pypp_cli.do.transpile.load_bridge_json.z.models import (
    AngleIncludeModel,
    CustomMappingValueModel,
    LeftAndRightValueModel,
    QuoteIncludeModel,
    ReplaceDotWithDoubleColonValueModel,
    RequiredPyImportModel,
    ToStringValueModel,
)
from pypp_cli.do.transpile.transpile.handle.z.d_types import (
    AngInc,
    CppInclude,
    PyImport,
    PySpecificImpFrom,
    PySpecificImport,
    QInc,
)
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import (
    CustomMappingFromLibEntry,
    CustomMappingStartsWithFromLibEntry,
    LeftAndRightEntry,
    ReplaceDotWithDoubleColonEntry,
    ToStringEntry,
)


def _calc_cpp_include(
    quote: QuoteIncludeModel | None, angle: AngleIncludeModel | None
) -> list[CppInclude]:
    ret: list[CppInclude] = []
    if quote is not None:
        for inc_str in quote.root:
            ret.append(QInc(inc_str))
    if angle is not None:
        for inc_str in angle.root:
            ret.append(AngInc(inc_str))
    return ret


def calc_required_py_import(
    d: RequiredPyImportModel | None,
) -> PySpecificImport | None:
    if d is not None:
        if d.module is not None:
            return PySpecificImpFrom(d.module, d.name)
        if d.as_name is not None:
            return PyImport(d.name, d.as_name)
        return PyImport(d.name)
    return None


def calc_imp_str(imp: PySpecificImport | None) -> str:
    return "" if imp is None else f" ({imp})"


def calc_to_string_entry(d: ToStringValueModel) -> ToStringEntry:
    return ToStringEntry(d.to, _calc_cpp_include(d.quote_includes, d.angle_includes))


def calc_custom_mapping_from_lib_entry(
    d: CustomMappingValueModel,
) -> CustomMappingFromLibEntry:
    return CustomMappingFromLibEntry(
        "\n".join(d.mapping_function),
        _calc_cpp_include(d.quote_includes, d.angle_includes),
    )


def calc_custom_mapping_starts_with_from_lib_entry(
    d: CustomMappingValueModel,
) -> CustomMappingStartsWithFromLibEntry:
    return CustomMappingStartsWithFromLibEntry(
        "\n".join(d.mapping_function),
        _calc_cpp_include(d.quote_includes, d.angle_includes),
    )


def calc_replace_dot_with_double_colon_entry(
    d: ReplaceDotWithDoubleColonValueModel,
) -> ReplaceDotWithDoubleColonEntry:
    return ReplaceDotWithDoubleColonEntry(
        _calc_cpp_include(d.quote_includes, d.angle_includes), False
    )


def calc_left_and_right_entry(obj: LeftAndRightValueModel) -> LeftAndRightEntry:
    return LeftAndRightEntry(
        obj.left, obj.right, _calc_cpp_include(obj.quote_includes, obj.angle_includes)
    )
