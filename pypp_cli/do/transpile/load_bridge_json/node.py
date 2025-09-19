from dataclasses import dataclass
import json
from pathlib import Path

from pydantic import ValidationError
from pypp_cli.do.transpile.load_bridge_json.z.models import (
    AlwaysPassByValueModel,
    AnnAssignModel,
    AttrModel,
    CMakeListsModel,
    CallModel,
    NameModel,
    SubscriptableTypeModel,
)
from pypp_cli.do.transpile.find_libs.z.find_all_libs import PyppLibs


@dataclass(frozen=True, slots=True)
class BridgeJsonModels:
    name_map: NameModel | None = None
    ann_assign_map: AnnAssignModel | None = None
    call_map: CallModel | None = None
    attr_map: AttrModel | None = None
    always_pass_by_value: AlwaysPassByValueModel | None = None
    subscriptable_types: SubscriptableTypeModel | None = None
    cmake_lists: CMakeListsModel | None = None


def load_all_bridge_jsons(
    libs: PyppLibs, site_packages_dir: Path
) -> dict[str, BridgeJsonModels]:
    ret = {}
    for lib in libs:
        verifier = _BridgeJsonLoader(site_packages_dir, lib)
        ret[lib] = verifier.load()
    return ret


@dataclass(frozen=True, slots=True)
class _BridgeJsonLoader:
    _site_packages_dir: Path
    _library_name: str

    def load(self) -> BridgeJsonModels:
        name_map: NameModel | None = None
        ann_assign_map: AnnAssignModel | None = None
        call_map: CallModel | None = None
        attr_map: AttrModel | None = None
        always_pass_by_value: AlwaysPassByValueModel | None = None
        subscriptable_types: SubscriptableTypeModel | None = None
        cmake_lists: CMakeListsModel | None = None
        for file_name in [
            "name_map",
            "ann_assign_map",
            "call_map",
            "attr_map",
            "always_pass_by_value",
            "subscriptable_types",
            "cmake_lists",
        ]:
            json_path: Path = self._calc_bridge_json(self._library_name, file_name)
            if json_path.exists():
                with open(json_path, "r") as f:
                    data = json.load(f)
                try:
                    if file_name == "name_map":
                        name_map = NameModel(**data)
                    elif file_name == "ann_assign_map":
                        ann_assign_map = AnnAssignModel(**data)
                    elif file_name == "call_map":
                        call_map = CallModel(**data)
                    elif file_name == "attr_map":
                        attr_map = AttrModel(**data)
                    elif file_name == "always_pass_by_value":
                        always_pass_by_value = AlwaysPassByValueModel(**data)
                    elif file_name == "subscriptable_types":
                        subscriptable_types = SubscriptableTypeModel(**data)
                    elif file_name == "cmake_lists":
                        cmake_lists = CMakeListsModel(**data)
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
            call_map,
            attr_map,
            always_pass_by_value,
            subscriptable_types,
            cmake_lists,
        )

    def _calc_bridge_json(self, library_name: str, json_file_name: str) -> Path:
        return (
            self._site_packages_dir
            / library_name
            / "pypp_data"
            / "bridge_jsons"
            / f"{json_file_name}.json"
        )
