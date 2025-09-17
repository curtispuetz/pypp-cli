from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.transpilers.proj.all_data.load_proj_info import load_metadata

# value indicates if it has bridge jsons or not
type PyppLibs = dict[str, bool]


@dataclass(frozen=True, slots=True)
class PyppLibsData:
    libs: PyppLibs
    namespaces: dict[str, str]  # lib name -> namespace


def find_libs(site_packages_dir: Path) -> PyppLibsData:
    if not site_packages_dir.is_dir():
        return PyppLibsData(libs={}, namespaces={})
    ret = PyppLibsData(libs={}, namespaces={})
    for entry in site_packages_dir.iterdir():
        if entry.is_dir() and not entry.name.endswith(".dist-info"):
            lib_pypp_data_dir = entry / "pypp_data"
            if lib_pypp_data_dir.is_dir():
                # found a Py++ library
                has_bridge_jsons = (
                    True if (lib_pypp_data_dir / "bridge_jsons").is_dir() else False
                )
                metadata_json = lib_pypp_data_dir / "metadata.json"
                if metadata_json.is_file():
                    metadata = load_metadata(lib_pypp_data_dir / "metadata.json")
                    ret.namespaces[entry.name] = metadata.namespace
                ret.libs[entry.name] = has_bridge_jsons
    return ret
