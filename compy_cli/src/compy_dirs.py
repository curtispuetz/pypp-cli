from pathlib import Path


# TODO: there should be a different CompyDirs for pure-libraries
class CompyDirs:
    def __init__(self, target_dir: Path):
        self.target_dir = target_dir
        self.resources_dir: Path = target_dir / "resources"
        self.cpp_dir: Path = target_dir / "cpp"
        self.cpp_build_dir: Path = self.cpp_dir / "build"
        self.cpp_build_release_dir: Path = self.cpp_build_dir / "Release"
        self.cpp_src_dir: Path = self.cpp_dir / "src"
        self.python_dir: Path = target_dir / "python"
        self.python_src_dir: Path = self.python_dir / "src"
        self.compy_data_dir: Path = target_dir / "compy_data"
        self.timestamps_file: Path = self.compy_data_dir / "file_timestamps.json"
        self.proj_info_file: Path = self.compy_data_dir / "proj_info.json"

    def calc_py_executable(self) -> Path:
        return self.python_dir / ".venv" / "Scripts" / "python.exe"

    def calc_site_packages_dir(self) -> Path:
        return self.python_dir / ".venv" / "Lib" / "site-packages"

    def calc_lib_py_executable(self) -> Path:
        return self.target_dir / ".venv" / "Scripts" / "python.exe"

    def calc_library_cpp_data_dir(self, library_name: str) -> Path:
        return self.calc_site_packages_dir() / library_name / "data" / "cpp"

    def calc_cpp_libs_dir(self, library_name: str) -> Path:
        return self.cpp_dir / "libs" / library_name

    def calc_bridge_json(self, library_name: str, json_file_name: str) -> Path:
        return (
            self.calc_site_packages_dir()
            / library_name
            / "data"
            / "bridge_jsons"
            / f"{json_file_name}.json"
        )

    def calc_pure_lib_dir(self, lib_dir_name: str) -> Path:
        return self.target_dir / lib_dir_name

    def calc_pure_lib_cpp_dir(self, lib_dir_name: str) -> Path:
        return self.calc_pure_lib_dir(lib_dir_name) / "cpp"

    def calc_pure_lib_compy_data_dir(self) -> Path:
        return self.target_dir / "compy_data"

    def calc_pure_lib_proj_info(self) -> Path:
        return self.calc_pure_lib_compy_data_dir() / "proj_info.json"

    def calc_pure_lib_timestamps_file(self) -> Path:
        return self.calc_pure_lib_compy_data_dir() / "file_timestamps.json"


def calc_bridge_json(
    py_env_parent_dir: Path, library_name: str, json_file_name: str
) -> Path:
    return (
        py_env_parent_dir
        / ".venv"
        / "Lib"
        / "site-packages"
        / library_name
        / "data"
        / "bridge_jsons"
        / f"{json_file_name}.json"
    )


def create_test_dir_compy_dirs() -> CompyDirs:
    return CompyDirs(Path(__file__).parent.parent / "test_dir")
