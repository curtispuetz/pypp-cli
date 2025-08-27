import json
from typing import Callable
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.d_types import (
    PySpecificImport,
)
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.mapping.maps.util.util import calc_imp_str, calc_required_py_import


def calc_map_2(
    default_map: dict[str, set[PySpecificImport | None]],
    proj_info: ProjInfo,
    dirs: CompyDirs,
    json_file_name: str,
    warning_fn: Callable[[str, str], str],
) -> dict[str, set[PySpecificImport | None]]:
    ret = default_map.copy()
    for installed_library in proj_info.installed_bridge_libs:
        json_path: Path = dirs.calc_bridge_json(installed_library, json_file_name)
        if json_path.is_file():
            with open(json_path, "r") as f:
                m: dict = json.load(f)
            for _type, obj in m.items():
                required_import = calc_required_py_import(obj)
                if _type in ret:
                    if required_import in ret[_type]:
                        print(
                            f"warning: {
                                warning_fn(
                                    installed_library,
                                    f'{_type}{calc_imp_str(required_import)}',
                                )
                            }"
                        )
                    ret[_type].add(required_import)
                else:
                    ret[_type] = {required_import}
    return ret
