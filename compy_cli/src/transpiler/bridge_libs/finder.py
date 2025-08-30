from pathlib import Path


def find_bridge_libs(site_packages_dir: Path) -> list[str]:
    ret = []
    for entry in site_packages_dir.iterdir():
        if entry.is_dir() and not entry.name.endswith(".dist-info"):
            bridge_jsons_dir = entry / "compy_data" / "bridge_jsons"
            if bridge_jsons_dir.is_dir():
                ret.append(entry.name)
    print("Found bridge libraries:", ret)
    return ret


def find_added_and_deleted_bridge_libs(
    cpp_dir: Path, bridge_libs: set[str]
) -> tuple[list[str], list[str]]:
    libs_dir: Path = cpp_dir / "libs"
    if not libs_dir.is_dir():
        return list(bridge_libs), []
    added = bridge_libs.copy()
    deleted = []
    for entry in libs_dir.iterdir():
        if entry.is_dir():
            if entry.name not in bridge_libs:
                deleted.append(entry.name)
            else:
                added.remove(entry.name)
    ret_added = list(added)
    print("New bridge libraries:", ret_added)
    print("Deleted bridge libraries:", deleted)
    return ret_added, deleted
