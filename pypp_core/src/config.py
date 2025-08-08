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
        self.timestamps_file: str = os.path.join(target_dir, "file_timestamps.json")


def create_test_dir_pypp_dirs() -> PyppDirs:
    return PyppDirs(os.path.join(os.path.dirname(__file__), "..", "test_dir"))
