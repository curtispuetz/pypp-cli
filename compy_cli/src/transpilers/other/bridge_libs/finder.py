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
