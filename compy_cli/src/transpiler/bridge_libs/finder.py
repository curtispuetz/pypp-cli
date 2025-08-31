from pathlib import Path


def find_libs(site_packages_dir: Path) -> tuple[list[str], list[str]]:
    bridge = []
    pure = []
    for entry in site_packages_dir.iterdir():
        if entry.is_dir() and not entry.name.endswith(".dist-info"):
            bridge_jsons_dir = entry / "compy_data" / "bridge_jsons"
            if bridge_jsons_dir.is_dir():
                bridge.append(entry.name)
            else:
                pure_cpp_dir = entry / "compy_cpp"
                if pure_cpp_dir.is_dir():
                    pure.append(entry.name)
    return bridge, pure


def find_added_and_deleted_libs(
    cpp_dir: Path, bridge_libs: list[str], pure_libs: list[str]
) -> tuple[list[str], list[str], list[str]]:
    libs_dir: Path = cpp_dir / "libs"
    if not libs_dir.is_dir():
        return bridge_libs, pure_libs, []
    bridge_libs_set = set(bridge_libs)
    pure_libs_set = set(pure_libs)
    added_bridge = bridge_libs_set.copy()
    added_pure = pure_libs_set.copy()
    deleted = []
    for entry in libs_dir.iterdir():
        if entry.is_dir():
            if entry.name not in bridge_libs_set and entry.name not in pure_libs_set:
                deleted.append(entry.name)
            else:
                added_bridge.discard(entry.name)
                added_pure.discard(entry.name)
    ret_bridge = list(added_bridge)
    ret_pure = list(added_pure)
    print("Found bridge libraries:", bridge_libs)
    print("New bridge libraries:", ret_bridge)
    print("Found pure libraries:", pure_libs)
    print("New pure libraries:", ret_pure)
    print("Deleted libraries:", deleted)
    return ret_bridge, ret_pure, deleted
