from dataclasses import dataclass
import json
from pathlib import Path
from typing import Callable

from pydantic_core import ValidationError

from pypp_cli.do.transpile.y.transpiler_config_models import (
    AlwaysPassByValueModel,
    AnnAssignModel,
    AttrModel,
    TranspilerConfigModels,
    CMakeListsModel,
    CallModel,
    NameModel,
    SubscriptableTypeModel,
)
from pypp_cli.y.constants import TRANSPILER_CONFIG_DIR


def load_transpiler_config_models[T](
    _dir: Path,
    path_cltr: Callable[[Path, T, str], Path],
    lib: T,
) -> TranspilerConfigModels:
    return _TranspilerConfigModelLoader(_dir, path_cltr, lib).load_models()


@dataclass(frozen=True, slots=True)
class _TranspilerConfigModelLoader[T]:
    _dir: Path
    _path_cltr: Callable[[Path, T, str], Path]
    _lib: T

    def load_models(self) -> TranspilerConfigModels:
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
                    if self._lib is None:
                        raise ValueError(
                            f"An issue was found in the project {file_name}.json file "
                            f"in the .pypp/{TRANSPILER_CONFIG_DIR} directory.\n"
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
        return TranspilerConfigModels(
            name_map,
            ann_assign_map,
            call_map,
            attr_map,
            always_pass_by_value,
            subscriptable_types,
            cmake_lists,
        )
