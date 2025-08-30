from dataclasses import dataclass
import json
from pathlib import Path
import shutil
from importlib.resources import files, as_file

from compy_cli.src.library.file_actions import rm_dirs_and_files
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo


@dataclass(frozen=True, slots=True)
class CppProjectInitializerDeps:
    cpp_dir: Path
    timestamps_file: Path
    proj_info_file: Path
    proj_info: ProjInfo


class CppProjectInitializer:
    def __init__(self, d: CppProjectInitializerDeps):
        self._d = d

    def initialize_of_cpp_dir_is_dirty(self):
        if self._d.proj_info.cpp_dir_is_dirty:
            self._initialize()
        else:
            print("C++ template already copied to the cpp project directory")

    def _initialize(self):
        rm_dirs_and_files(self._d.cpp_dir, {"libs"})
        self._copy_cpp_template_to_cpp_dir()
        # Need to remove the timestamps file because all the C++ files need to be
        # generated again.
        if self._d.timestamps_file.exists():
            self._d.timestamps_file.unlink()
        self._set_cpp_dir_not_dirty_in_json()

    def _set_cpp_dir_not_dirty_in_json(self):
        with open(self._d.proj_info_file, "w") as file:
            json.dump(
                {
                    "cpp_dir_is_dirty": False,
                    "ignore_src_files": self._d.proj_info.ignored_src_files,
                    "ignore_main_files": self._d.proj_info.ignored_main_files,
                    "installed_"
                    "bridge_libraries": self._d.proj_info.installed_bridge_libs,
                },
                file,
                indent=4,
            )

    def _copy_cpp_template_to_cpp_dir(self):
        print("Copying the C++ template to the cpp project directory")
        # Copy files and directories from the template
        template_root = files("compy_cli.data.cpp_template")
        for item in template_root.iterdir():
            with as_file(item) as src_path:
                dst_path: Path = self._d.cpp_dir / item.name
                if src_path.is_dir():
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
