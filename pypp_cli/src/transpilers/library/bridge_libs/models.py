from pydantic import BaseModel, RootModel


class QuoteIncludeModel(RootModel[list[str]]):
    pass


class AngleIncludeModel(RootModel[list[str]]):
    pass


class RequiredPyImportModel(BaseModel):
    name: str
    module: str | None = None
    as_name: str | None = None


class ToStringValueModel(BaseModel):
    to: str
    quote_includes: QuoteIncludeModel | None = None
    angle_includes: AngleIncludeModel | None = None
    required_py_import: RequiredPyImportModel | None = None


class CustomMappingValueModel(BaseModel):
    mapping_function: list[str]
    quote_includes: QuoteIncludeModel | None = None
    angle_includes: AngleIncludeModel | None = None
    required_py_import: RequiredPyImportModel | None = None


class ReplaceDotWithDoubleColonValueModel(BaseModel):
    quote_includes: QuoteIncludeModel | None = None
    angle_includes: AngleIncludeModel | None = None
    required_py_import: RequiredPyImportModel | None = None


class ToStringModel(RootModel[dict[str, ToStringValueModel]]):
    pass


class CustomMappingModel(RootModel[dict[str, CustomMappingValueModel]]):
    pass


class ReplaceDotWithDoubleColonModel(
    RootModel[dict[str, ReplaceDotWithDoubleColonValueModel]]
):
    pass


class NameModel(BaseModel):
    to_string: ToStringModel | None = None
    custom_mapping: CustomMappingModel | None = None
    custom_mapping_starts_with: CustomMappingModel | None = None


class CallModel(BaseModel):
    to_string: ToStringModel | None = None
    custom_mapping: CustomMappingModel | None = None
    custom_mapping_starts_with: CustomMappingModel | None = None
    replace_dot_with_double_colon: ReplaceDotWithDoubleColonModel | None = None


class AttrModel(BaseModel):
    to_string: ToStringModel | None = None
    custom_mapping: CustomMappingModel | None = None
    custom_mapping_starts_with: CustomMappingModel | None = None
    replace_dot_with_double_colon: ReplaceDotWithDoubleColonModel | None = None


class AnnAssignModel(BaseModel):
    custom_mapping: CustomMappingModel | None = None
    custom_mapping_starts_with: CustomMappingModel | None = None


class AlwaysPassByValueValueModel(BaseModel):
    required_py_import: RequiredPyImportModel | None = None


class AlwaysPassByValueModel(RootModel[dict[str, AlwaysPassByValueValueModel | None]]):
    pass


class SubscriptableTypeValueModel(BaseModel):
    required_py_import: RequiredPyImportModel | None = None


class SubscriptableTypeModel(RootModel[dict[str, SubscriptableTypeValueModel | None]]):
    pass


class ImportModel(BaseModel):
    direct_to_cpp_include: list[str] | None = None
    ignore: list[str] | None = None


class CMakeListsModel(BaseModel):
    add_lines: list[str] | None = None
    link_libraries: list[str] | None = None


BRIDGE_JSON_MODELS: dict[str, type] = {
    "name_map": NameModel,
    "ann_assign_map": AnnAssignModel,
    "import_map": ImportModel,
    "call_map": CallModel,
    "attr_map": AttrModel,
    "subscriptable_types": SubscriptableTypeModel,
    "always_pass_by_value": AlwaysPassByValueModel,
    "cmake_lists": CMakeListsModel,
}


if __name__ == "__main__":
    data = {"name": "test", "module": "mod"}
    RequiredPyImportModel(**data)
