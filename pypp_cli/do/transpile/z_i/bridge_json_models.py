from dataclasses import dataclass
from pydantic import BaseModel, RootModel


class QuoteIncludeModel(RootModel[list[str]]):
    pass


class AngleIncludeModel(RootModel[list[str]]):
    pass


class RequiredPyImportModel(BaseModel):
    name: str
    module: str | None = None
    as_name: str | None = None
    model_config = {"extra": "forbid"}


class ToStringValueModel(BaseModel):
    to: str
    quote_includes: QuoteIncludeModel | None = None
    angle_includes: AngleIncludeModel | None = None
    required_py_import: RequiredPyImportModel | None = None
    model_config = {"extra": "forbid"}


class LeftAndRightValueModel(BaseModel):
    left: str
    right: str
    quote_includes: QuoteIncludeModel | None = None
    angle_includes: AngleIncludeModel | None = None
    required_py_import: RequiredPyImportModel | None = None
    model_config = {"extra": "forbid"}


class CustomMappingValueModel(BaseModel):
    mapping_function: list[str]
    quote_includes: QuoteIncludeModel | None = None
    angle_includes: AngleIncludeModel | None = None
    required_py_import: RequiredPyImportModel | None = None
    model_config = {"extra": "forbid"}


class ReplaceDotWithDoubleColonValueModel(BaseModel):
    quote_includes: QuoteIncludeModel | None = None
    angle_includes: AngleIncludeModel | None = None
    required_py_import: RequiredPyImportModel | None = None
    model_config = {"extra": "forbid"}


class ToStringModel(RootModel[dict[str, ToStringValueModel]]):
    pass


class LeftAndRightModel(RootModel[dict[str, LeftAndRightValueModel]]):
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
    model_config = {"extra": "forbid"}


class CallModel(BaseModel):
    left_and_right: LeftAndRightModel | None = None
    to_string: ToStringModel | None = None
    custom_mapping: CustomMappingModel | None = None
    custom_mapping_starts_with: CustomMappingModel | None = None
    replace_dot_with_double_colon: ReplaceDotWithDoubleColonModel | None = None
    model_config = {"extra": "forbid"}


class AttrModel(BaseModel):
    to_string: ToStringModel | None = None
    custom_mapping: CustomMappingModel | None = None
    custom_mapping_starts_with: CustomMappingModel | None = None
    replace_dot_with_double_colon: ReplaceDotWithDoubleColonModel | None = None
    model_config = {"extra": "forbid"}


class AnnAssignModel(BaseModel):
    custom_mapping: CustomMappingModel | None = None
    custom_mapping_starts_with: CustomMappingModel | None = None
    model_config = {"extra": "forbid"}


class AlwaysPassByValueValueModel(BaseModel):
    required_py_import: RequiredPyImportModel | None = None
    model_config = {"extra": "forbid"}


class AlwaysPassByValueModel(RootModel[dict[str, AlwaysPassByValueValueModel | None]]):
    pass


class SubscriptableTypeValueModel(BaseModel):
    required_py_import: RequiredPyImportModel | None = None
    model_config = {"extra": "forbid"}


class SubscriptableTypeModel(RootModel[dict[str, SubscriptableTypeValueModel | None]]):
    pass


class CMakeListsModel(BaseModel):
    add_lines: list[str] | None = None
    link_libraries: list[str] | None = None
    model_config = {"extra": "forbid"}


@dataclass(frozen=True, slots=True)
class BridgeJsonModels:
    name_map: NameModel | None = None
    ann_assign_map: AnnAssignModel | None = None
    call_map: CallModel | None = None
    attr_map: AttrModel | None = None
    always_pass_by_value: AlwaysPassByValueModel | None = None
    subscriptable_types: SubscriptableTypeModel | None = None
    cmake_lists: CMakeListsModel | None = None


type BridgeJsonModelsDict = dict[str | None, BridgeJsonModels]
