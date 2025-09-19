from pypp_cli.do.transpile.y.transpiler_config_models import (
    AngleIncludeModel,
    TranspilerConfigModelsDict,
    CustomMappingValueModel,
    LeftAndRightValueModel,
    QuoteIncludeModel,
    RequiredPyImportModel,
    ToStringValueModel,
)
from pypp_cli.do.transpile.transpile.y.d_types import (
    AngInc,
    CppInclude,
    PyImp,
    QInc,
)
from pypp_cli.do.transpile.transpile.y.maps.d_types import (
    CustomMappingFromLibEntry,
    CustomMappingStartsWithFromLibEntry,
    LeftAndRightEntry,
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
) -> PyImp | None:
    if d is not None:
        return PyImp(d.module, d.name)
    return None


def calc_imp_str(imp: PyImp | None) -> str:
    return "" if imp is None else f" ({imp})"


def calc_to_string_entry(d: ToStringValueModel) -> ToStringEntry:
    return ToStringEntry(d.to, _calc_cpp_include(d.quote_includes, d.angle_includes))


def calc_custom_mapping_from_lib_entry(
    transpiler_config_models: TranspilerConfigModelsDict,
    lib: str | None,
    d: CustomMappingValueModel,
) -> CustomMappingFromLibEntry:
    s = transpiler_config_models[lib].mapping_functions[d.mapping_function]
    return CustomMappingFromLibEntry(
        s, _calc_cpp_include(d.quote_includes, d.angle_includes)
    )


def calc_custom_mapping_starts_with_from_lib_entry(
    transpiler_config_models: TranspilerConfigModelsDict,
    lib: str | None,
    d: CustomMappingValueModel,
) -> CustomMappingStartsWithFromLibEntry:
    s = transpiler_config_models[lib].mapping_functions[d.mapping_function]
    return CustomMappingStartsWithFromLibEntry(
        s, _calc_cpp_include(d.quote_includes, d.angle_includes)
    )


def calc_left_and_right_entry(obj: LeftAndRightValueModel) -> LeftAndRightEntry:
    return LeftAndRightEntry(
        obj.left, obj.right, _calc_cpp_include(obj.quote_includes, obj.angle_includes)
    )
