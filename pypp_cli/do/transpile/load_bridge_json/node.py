from pathlib import Path
from typing import Callable

from pypp_cli.do.transpile.load_bridge_json.z.load_mapping_fns import (
    load_mapping_functions,
)
from pypp_cli.do.transpile.load_bridge_json.z.load_models import load_bridge_json_models
from pypp_cli.do.transpile.z_i.bridge_json_models import (
    BridgeJsonModelsAndMappingFunctions,
    BridgeJsonModelsDict,
)
from pypp_cli.do.transpile.find_libs.z.find_all_libs import PyppLibs


def load_all_bridge_jsons(
    libs: PyppLibs, site_packages_dir: Path, proj_bridge_jsons_dir: Path
) -> BridgeJsonModelsDict:
    ret: BridgeJsonModelsDict = {}
    for lib in libs:
        ret[lib] = _load_val(
            site_packages_dir,
            _calc_bridge_json_for_lib,
            lib,
            site_packages_dir
            / lib
            / "pypp_data"
            / "bridge_jsons"
            / "mapping_functions",
        )
    ret[None] = _load_val(
        proj_bridge_jsons_dir,
        _calc_bridge_json_for_proj,
        None,
        proj_bridge_jsons_dir / "mapping_functions",
    )
    return ret


def _load_val[T](
    dir: Path, path_cltr: Callable[[Path, T, str], Path], lib: T, mapping_fn_dir: Path
) -> BridgeJsonModelsAndMappingFunctions:
    models = load_bridge_json_models(dir, path_cltr, lib)
    mapping_fns = load_mapping_functions(mapping_fn_dir)
    return BridgeJsonModelsAndMappingFunctions(models, mapping_fns)


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
