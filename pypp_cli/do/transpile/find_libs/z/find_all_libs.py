import json
from dataclasses import dataclass
from pathlib import Path

from pydantic import ValidationError
from pypp_cli.do.transpile.y.proj_metadata import ProjMetadata
from pypp_cli.y.constants import TRANSPILER_CONFIG_DIR

# value indicates if it has transpiler config or not
type PyppLibs = dict[str, bool]


@dataclass(frozen=True, slots=True)
class PyppLibsData:
    libs: PyppLibs
    namespaces: dict[str, str]  # lib name -> namespace


def find_all_libs(site_packages_dir: Path | None) -> PyppLibsData:
    if site_packages_dir is None or not site_packages_dir.is_dir():
        return PyppLibsData(libs={}, namespaces={})
    ret = PyppLibsData(libs={}, namespaces={})
    for entry in site_packages_dir.iterdir():
        if entry.is_dir() and not entry.name.endswith(".dist-info"):
            lib_pypp_data_dir = entry / "pypp_data"
            if lib_pypp_data_dir.is_dir():
                # found a Py++ library
                has_transpiler_config = (
                    True
                    if (lib_pypp_data_dir / TRANSPILER_CONFIG_DIR).is_dir()
                    else False
                )
                metadata_json = lib_pypp_data_dir / "metadata.json"
                if metadata_json.is_file():
                    metadata = _load_metadata(lib_pypp_data_dir / "metadata.json")
                    ret.namespaces[entry.name] = metadata.namespace
                ret.libs[entry.name] = has_transpiler_config
    return ret


def _load_metadata(metadata_file: Path) -> ProjMetadata:
    with open(metadata_file) as file:
        metadata = json.load(file)
    try:
        return ProjMetadata(**metadata)
    except ValidationError as e:
        raise ValueError(f"Issue found in metadata.json file: {e}") from e
