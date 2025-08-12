import os

dirname: str = os.path.dirname(__file__)


class PyppDirs:
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.resources_dir: str = os.path.join(target_dir, "resources")
        self.cpp_dir: str = os.path.join(target_dir, "cpp")
        self.cpp_build_dir: str = os.path.join(self.cpp_dir, "build")
        self.cpp_build_release_dir: str = os.path.join(self.cpp_build_dir, "Release")
        self.cpp_src_dir: str = os.path.join(self.cpp_dir, "src")
        self.python_dir: str = os.path.join(target_dir, "python")
        self.python_src_dir: str = os.path.join(self.python_dir, "src")
        self.pypp_data_dir: str = os.path.join(target_dir, "pypp_data")
        self.timestamps_file: str = os.path.join(
            self.pypp_data_dir, "file_timestamps.json"
        )
        self.proj_info_file: str = os.path.join(self.pypp_data_dir, "proj_info.json")

    def calc_py_executable(self) -> str:
        return os.path.join(self.python_dir, ".venv", "Scripts", "python.exe")

    def calc_site_packages_dir(self) -> str:
        return os.path.join(self.python_dir, ".venv", "Lib", "site-packages")

    def calc_library_cpp_data_dir(self, library_name: str) -> str:
        return os.path.join(self.calc_site_packages_dir(), library_name, "data", "cpp")

    def calc_cpp_libs_dir(self, library_name: str) -> str:
        return os.path.join(self.cpp_dir, "libs", library_name)

    def calc_bridge_json(self, library_name: str, json_file_name: str) -> str:
        return os.path.join(
            self.calc_site_packages_dir(),
            library_name,
            "data",
            "bridge_jsons",
            json_file_name + ".json",
        )


def create_test_dir_pypp_dirs() -> PyppDirs:
    return PyppDirs(os.path.join(os.path.dirname(__file__), "..", "test_dir"))
