from pathlib import Path

# value indicates if it has bridge jsons or not
type PyppLibs = dict[str, bool]


def find_libs(site_packages_dir: Path) -> PyppLibs:
    if not site_packages_dir.is_dir():
        return {}
    ret: PyppLibs = {}
    for entry in site_packages_dir.iterdir():
        if entry.is_dir() and not entry.name.endswith(".dist-info"):
            pypp_dir = entry / "pypp_data"
            if pypp_dir.is_dir():
                # found a Py++ library
                has_bridge_jsons = (
                    True if (pypp_dir / "bridge_jsons").is_dir() else False
                )
                assert (pypp_dir / "cpp").is_dir(), (
                    f"Library {entry.name} has no cpp directory in `pypp_data` folder"
                )
                ret[entry.name] = has_bridge_jsons
    return ret
