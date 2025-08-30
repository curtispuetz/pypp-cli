from pathlib import Path


class CompyDirsCltr:
    def __init__(self, target_dir: Path):
        self._t = target_dir

    @property
    def target_dir(self) -> Path:
        return self._t

    def calc_cpp_dir(self) -> Path:
        return self._t / "cpp"

    def calc_cpp_src_dir(self) -> Path:
        return self.calc_cpp_dir() / "src"

    def calc_cpp_build_dir(self) -> Path:
        return self.calc_cpp_dir() / "build"

    def calc_cpp_libs_dir(self, library_name: str) -> Path:
        return self.calc_cpp_dir() / "libs" / library_name

    def calc_cpp_build_release_dir(self) -> Path:
        return self.calc_cpp_build_dir() / "release"

    def calc_python_dir(self) -> Path:
        return self._t / "python"

    def calc_python_src_dir(self) -> Path:
        return self.calc_python_dir() / "src"

    def calc_compy_data_dir(self) -> Path:
        return self._t / "compy_data"

    def calc_timestamps_file(self) -> Path:
        return self.calc_compy_data_dir() / "file_timestamps.json"

    def calc_proj_info_file(self) -> Path:
        return self.calc_compy_data_dir() / "proj_info.json"

    def calc_py_executable(self) -> Path:
        return self.calc_python_dir() / ".venv" / "Scripts" / "python.exe"

    def calc_resources_dir(self) -> Path:
        return self._t / "resources"

    def calc_lib_py_executable(self) -> Path:
        return self.target_dir / ".venv" / "Scripts" / "python.exe"

    def calc_site_packages_dir(self) -> Path:
        return self.calc_python_dir() / ".venv" / "Lib" / "site-packages"

    def calc_library_cpp_data_dir(self, library_name: str) -> Path:
        return self.calc_site_packages_dir() / library_name / "data" / "cpp"
