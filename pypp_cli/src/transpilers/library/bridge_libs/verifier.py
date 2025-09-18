from dataclasses import dataclass
import json
from pathlib import Path

from pydantic import ValidationError
from pypp_cli.src.transpilers.library.bridge_libs.models import (
    AlwaysPassByValueModel,
    AnnAssignModel,
    AttrModel,
    CallModel,
    ImportModel,
    NameModel,
    SubscriptableTypeModel,
)
from pypp_cli.src.transpilers.library.bridge_libs.finder import PyppLibs
from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)


@dataclass(frozen=True, slots=True)
class BridgeJsonModels:
    name_map: NameModel | None = None
    ann_assign_map: AnnAssignModel | None = None
    import_map: ImportModel | None = None
    call_map: CallModel | None = None
    attr_map: AttrModel | None = None
    always_pass_by_value: AlwaysPassByValueModel | None = None
    subscriptable_types: SubscriptableTypeModel | None = None


def verify_all_bridge_jsons(
    libs: PyppLibs, bridge_json_path_cltr: BridgeJsonPathCltr
) -> dict[str, BridgeJsonModels]:
    ret = {}
    for lib in libs:
        verifier = _BridgeJsonVerifier(bridge_json_path_cltr, lib)
        ret[lib] = verifier.verify_bridge_jsons()
    if len(libs) > 0:
        print("Verified all bridge JSON files in libraries")
    return ret


# TODO: rename to "loader"
@dataclass(frozen=True, slots=True)
class _BridgeJsonVerifier:
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _library_name: str

    def verify_bridge_jsons(self) -> BridgeJsonModels:
        name_map: NameModel | None = None
        ann_assign_map: AnnAssignModel | None = None
        import_map: ImportModel | None = None
        call_map: CallModel | None = None
        attr_map: AttrModel | None = None
        always_pass_by_value: AlwaysPassByValueModel | None = None
        subscriptable_types: SubscriptableTypeModel | None = None
        for file_name in [
            "name_map",
            "ann_assign_map",
            "import_map",
            "call_map",
            "attr_map",
            "always_pass_by_value",
            "subscriptable_types",
        ]:
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                self._library_name, file_name
            )
            if json_path.exists():
                with open(json_path, "r") as f:
                    data = json.load(f)
                try:
                    if file_name == "name_map":
                        name_map = NameModel(**data)
                    elif file_name == "ann_assign_map":
                        ann_assign_map = AnnAssignModel(**data)
                    elif file_name == "import_map":
                        import_map = ImportModel(**data)
                    elif file_name == "call_map":
                        call_map = CallModel(**data)
                    elif file_name == "attr_map":
                        attr_map = AttrModel(**data)
                    elif file_name == "always_pass_by_value":
                        always_pass_by_value = AlwaysPassByValueModel(**data)
                    elif file_name == "subscriptable_types":
                        subscriptable_types = SubscriptableTypeModel(**data)
                except ValidationError as e:
                    raise ValueError(
                        f"An issue was found in the {file_name}.json file in "
                        f"library {self._library_name}. The issue needs to be fixed in "
                        f"the library and then it can be reinstalled. "
                        f"The pydantic validation error:"
                        f"\n{e}"
                    )
        return BridgeJsonModels(
            name_map,
            ann_assign_map,
            import_map,
            call_map,
            attr_map,
            always_pass_by_value,
            subscriptable_types,
        )
