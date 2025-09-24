from pathlib import Path
from typing import Callable

from pypp_cli.do.transpile.load_transpiler_config.z.load_mapping_fns import (
    load_mapping_functions,
)
from pypp_cli.do.transpile.load_transpiler_config.z.load_models import (
    load_transpiler_config_models,
)
from pypp_cli.do.transpile.y.transpiler_config_models import (
    TranspilerConfigModelsAndMappingFunctions,
    TranspilerConfigModelsDict,
)
from pypp_cli.do.transpile.find_libs.z.find_all_libs import PyppLibs
from pypp_cli.y.constants import TRANSPILER_CONFIG_DIR


def load_transpiler_config(
    libs: PyppLibs, site_packages_dir: Path | None, proj_transpiler_config_dir: Path
) -> TranspilerConfigModelsDict:
    ret: TranspilerConfigModelsDict = {}
    if site_packages_dir is not None:
        for lib in libs:
            ret[lib] = _load_val(
                site_packages_dir,
                _calc_transpiler_config_for_lib,
                lib,
                site_packages_dir
                / lib
                / "pypp_data"
                / TRANSPILER_CONFIG_DIR
                / "mapping_functions",
            )
    ret[None] = _load_val(
        proj_transpiler_config_dir,
        _calc_transpiler_config_for_proj,
        None,
        proj_transpiler_config_dir / "mapping_functions",
    )
    return ret


def _load_val[T](
    dir: Path, path_cltr: Callable[[Path, T, str], Path], lib: T, mapping_fn_dir: Path
) -> TranspilerConfigModelsAndMappingFunctions:
    models = load_transpiler_config_models(dir, path_cltr, lib)
    mapping_fns = load_mapping_functions(mapping_fn_dir)
    return TranspilerConfigModelsAndMappingFunctions(models, mapping_fns)


def _calc_transpiler_config_for_lib(
    site_packages_dir: Path, lib: str, json_file_name: str
) -> Path:
    return (
        site_packages_dir
        / lib
        / "pypp_data"
        / TRANSPILER_CONFIG_DIR
        / f"{json_file_name}.json"
    )


def _calc_transpiler_config_for_proj(
    proj_transpiler_config_dir: Path, _lib: None, json_file_name: str
) -> Path:
    return proj_transpiler_config_dir / f"{json_file_name}.json"
