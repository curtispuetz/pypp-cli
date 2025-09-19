from dataclasses import dataclass
import json
from pathlib import Path
import shutil
from importlib.resources import files, as_file

from pypp_cli.src.config import ProjInfo
from pypp_cli.library.file_actions import rm_dirs_and_files


@dataclass(frozen=True, slots=True)
class CppProjectInitializer:
    _cpp_dir: Path
    _timestamps_file: Path
    _proj_info_file: Path
    _proj_info: ProjInfo

    def initialize_if_cpp_dir_is_dirty(self):
        if self._proj_info.cpp_dir_is_dirty:
            self._initialize()
        else:
            print(
                "Not copying C++ template to the cpp project directory. Already copied."
            )

    def _initialize(self):
        if not self._cpp_dir.exists():
            self._cpp_dir.mkdir(parents=True)
        rm_dirs_and_files(self._cpp_dir, {"libs"})
        self._copy_cpp_template_to_cpp_dir()
        # Need to remove the timestamps file because all the C++ files need to be
        # generated again.
        if self._timestamps_file.exists():
            self._timestamps_file.unlink()
        self._set_cpp_dir_not_dirty_in_json()

    def _set_cpp_dir_not_dirty_in_json(self):
        self._proj_info.cpp_dir_is_dirty = False
        with open(self._proj_info_file, "w") as file:
            json.dump(
                self._proj_info.model_dump(),
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
