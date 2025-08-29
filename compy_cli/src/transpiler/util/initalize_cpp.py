from dataclasses import dataclass
import json
from pathlib import Path
import shutil
from importlib.resources import files, as_file

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.library.file_actions import rm_dirs_and_files
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo


@dataclass(frozen=True, slots=True)
class CppProjectInitializerDeps:
    dirs: CompyDirs
    proj_info: ProjInfo


class CppProjectInitializer:
    def __init__(self, d: CppProjectInitializerDeps):
        self.d = d

    def initialize(self):
        rm_dirs_and_files(self.d.dirs.cpp_dir, {"libs"})
        self._copy_cpp_template_to_cpp_dir()
        # Need to remove the timestamps file because all the C++ files need to be
        # generated again.
        if self.d.dirs.timestamps_file.exists():
            self.d.dirs.timestamps_file.unlink()
        self._set_cpp_dir_not_dirty_in_json()

    def _set_cpp_dir_not_dirty_in_json(self):
        with open(self.d.dirs.proj_info_file, "w") as file:
            json.dump(
                {
                    "cpp_dir_is_dirty": False,
                    "ignore_src_files": self.d.proj_info.ignored_src_files,
                    "ignore_main_files": self.d.proj_info.ignored_main_files,
                    "installed_"
                    "bridge_libraries": self.d.proj_info.installed_bridge_libs,
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
                dst_path: Path = self.d.dirs.cpp_dir / item.name
                if src_path.is_dir():
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
