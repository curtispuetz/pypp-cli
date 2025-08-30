from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class InitBridgeLibraryPaths:
    lib_py_executable: Path
    python_dir: Path
    cpp_dir: Path
    hello_world_h: Path
    hello_world_cpp: Path
    bridge_jsons_dir: Path
    import_map_json: Path


def create_init_bridge_lib_compy_paths(
    target_dir: Path, python_dir_name: str
) -> InitBridgeLibraryPaths:
    python_dir = target_dir / python_dir_name
    compy_data_dir = python_dir / "compy_data"
    cpp_dir = compy_data_dir / "cpp"
    bridge_jsons_dir = compy_data_dir / "bridge_jsons"
    return InitBridgeLibraryPaths(
        target_dir / ".venv" / "Scripts" / "python.exe",
        python_dir,
        cpp_dir,
        cpp_dir / "hello_world.h",
        cpp_dir / "hello_world.cpp",
        bridge_jsons_dir,
        bridge_jsons_dir / "import_map.json",
    )
