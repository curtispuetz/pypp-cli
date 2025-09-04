from dataclasses import dataclass
import json
from pathlib import Path
import shutil
from importlib.resources import files, as_file

from pypp_cli.src.other.library.file_actions import rm_dirs_and_files
from pypp_cli.src.transpilers.proj.other.load_proj_info import ProjInfo


@dataclass(frozen=True, slots=True)
class CppProjectInitializer:
    _cpp_dir: Path
    _timestamps_file: Path
    _proj_info_file: Path
    _proj_info: ProjInfo

    def initialize_of_cpp_dir_is_dirty(self):
        if self._proj_info.cpp_dir_is_dirty:
            self._initialize()
        else:
            print(
                "Not copying C++ template to the cpp project directory. Already copied."
            )

    def _initialize(self):
        rm_dirs_and_files(self._cpp_dir, {"libs"})
        self._copy_cpp_template_to_cpp_dir()
        # Need to remove the timestamps file because all the C++ files need to be
        # generated again.
        if self._timestamps_file.exists():
            self._timestamps_file.unlink()
        self._set_cpp_dir_not_dirty_in_json()

    def _set_cpp_dir_not_dirty_in_json(self):
        with open(self._proj_info_file, "w") as file:
            json.dump(
                {
                    "cpp_dir_is_dirty": False,
                    "ignore_src_files": self._proj_info.ignored_src_files,
                    "ignore_main_files": self._proj_info.ignored_main_files,
                },
                file,
                indent=4,
            )

    def _copy_cpp_template_to_cpp_dir(self):
        print("Copying the C++ template to the cpp project directory")
        # Copy files and directories from the template
        template_root = files("pypp_cli.data.cpp_template")
        for item in template_root.iterdir():
            with as_file(item) as src_path:
                dst_path: Path = self._cpp_dir / item.name
                if src_path.is_dir():
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
