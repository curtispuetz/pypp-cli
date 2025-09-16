from pathlib import Path
import shutil
from dataclasses import dataclass

from pypp_cli.src.transpilers.proj.all_data.bridge_libs.util import calc_cpp_libs_dir


def delete_all_cpp_lib_files(cpp_dir: Path, lib_names: list[str]):
    d = _Deleter(cpp_dir, lib_names)
    d.delete()


@dataclass(frozen=True, slots=True)
class _Deleter:
    _cpp_dir: Path
    _lib_names: list[str]

    def delete(self):
        for lib_name in self._lib_names:
            self._delete_cpp_lib_files(lib_name)
        if len(self._lib_names) > 0:
            # note: This line comes right after deleted libraries are listed.
            print(
                "Deleted C++ lib files in cpp project directory for deleted libraries"
            )

    def _delete_cpp_lib_files(self, lib_name: str):
        dest_dir = calc_cpp_libs_dir(self._cpp_dir, lib_name)
        if dest_dir.exists():
            shutil.rmtree(dest_dir)
