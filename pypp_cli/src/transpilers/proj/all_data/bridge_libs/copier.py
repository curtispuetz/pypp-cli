from dataclasses import dataclass
from pathlib import Path
import shutil

from pypp_cli.src.transpilers.proj.all_data.bridge_libs.util import (
    calc_cpp_libs_dir,
    calc_library_cpp_data_dir,
)


def copy_all_lib_cpp_files(cpp_dir: Path, site_packages_dir: Path, new_libs: set[str]):
    copier = _CppLibCopier(cpp_dir, site_packages_dir)
    copier.copy_all(new_libs)
    if len(new_libs) > 0:
        print("Copied C++ lib files to cpp project directory for new libraries")


@dataclass(slots=True)
class _CppLibCopier:
    _cpp_dir: Path
    _site_packages_dir: Path

    def copy_all(self, new_libs: set[str]):
        for library_name in new_libs:
            self._copy_cpp_lib_files_if_any(library_name)

    def _copy_cpp_lib_files_if_any(self, library_name: str):
        src_dir = calc_library_cpp_data_dir(self._site_packages_dir, library_name)
        dest_dir = calc_cpp_libs_dir(self._cpp_dir, library_name)
        if dest_dir.exists():
            shutil.rmtree(dest_dir)
        if src_dir.exists():
            shutil.copytree(src_dir, dest_dir)
        else:
            # bridge library case
            # write a .txt file that says 'empty'
            dest_dir.mkdir(parents=True, exist_ok=True)
            (dest_dir / "empty.txt").write_text(
                f"No C++ source files for library {library_name}"
            )
