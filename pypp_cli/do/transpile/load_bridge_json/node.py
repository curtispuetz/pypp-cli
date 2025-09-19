from dataclasses import dataclass
import json
from pathlib import Path
from typing import Callable

from pydantic import ValidationError
from pypp_cli.do.transpile.z_i.bridge_json_models import (
    AlwaysPassByValueModel,
    AnnAssignModel,
    AttrModel,
    BridgeJsonModelsDict,
    CMakeListsModel,
    CallModel,
    NameModel,
    SubscriptableTypeModel,
)
from pypp_cli.do.transpile.find_libs.z.find_all_libs import PyppLibs
from pypp_cli.do.transpile.z_i.bridge_json_models import BridgeJsonModels


def load_all_bridge_jsons(
    libs: PyppLibs, site_packages_dir: Path, proj_bridge_jsons_dir: Path
) -> BridgeJsonModelsDict:
    ret = {}
    for lib in libs:
        verifier = _BridgeJsonLoader(site_packages_dir, _calc_bridge_json_for_lib, lib)
        ret[lib] = verifier.load()
    verifier = _BridgeJsonLoader(
        proj_bridge_jsons_dir, _calc_bridge_json_for_proj, None
    )
    ret[None] = verifier.load()
    return ret


def _calc_bridge_json_for_lib(
    site_packages_dir: Path, lib: str, json_file_name: str
) -> Path:
    return (
        site_packages_dir
        / lib
        / "pypp_data"
        / "bridge_jsons"
        / f"{json_file_name}.json"
    )


def _calc_bridge_json_for_proj(
    proj_bridge_jsons_dir: Path, _lib: None, json_file_name: str
) -> Path:
    return proj_bridge_jsons_dir / f"{json_file_name}.json"


@dataclass(frozen=True, slots=True)
class _BridgeJsonLoader[T]:
    _dir: Path
    _path_cltr: Callable[[Path, T, str], Path]
    _lib: T

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
            json_path: Path = self._path_cltr(self._dir, self._lib, file_name)
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
                    # TODO now: Different message if _lib is None
                    if self._lib is None:
                        raise ValueError(
                            f"An issue was found in the project {file_name}.json file "
                            f"in the .pypp/bridge_jsons directory.\n"
                            f"The pydantic validation error:"
                            f"\n\n{e}"
                        )
                    raise ValueError(
                        f"An issue was found in the {file_name}.json file in "
                        f"library {self._lib}. The issue needs to be fixed in "
                        f"the library and then it can be reinstalled.\n"
                        f"The pydantic validation error:"
                        f"\n\n{e}"
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
