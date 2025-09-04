from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import Callable

from pypp_cli.src.transpilers.proj.bridge_libs.util import (
    calc_cpp_libs_dir,
    calc_library_cpp_data_dir,
)


def copy_all_lib_cpp_files(
    cpp_dir: Path, site_packages_dir: Path, bridge_libs: list[str], pure_libs: list[str]
):
    copier = _CppLibCopier(cpp_dir, site_packages_dir)
    copier.copy_all_bridge_lib_cpp_files(bridge_libs)
    copier.copy_all_pure_lib_cpp_files(pure_libs)
    if len(bridge_libs) > 0 or len(pure_libs) > 0:
        print("Copied C++ lib files to cpp project directory for new libraries")


@dataclass(frozen=True, slots=True)
class _CppLibCopier:
    _cpp_dir: Path
    _site_packages_dir: Path

    def copy_all_bridge_lib_cpp_files(self, libs: list[str]):
        self._copy_all(libs, calc_library_cpp_data_dir)

    def copy_all_pure_lib_cpp_files(self, libs: list[str]):
        self._copy_all(
            libs,
            lambda site_packages_dir, lib_name: site_packages_dir
            / lib_name
            / "pypp_cpp",
        )

    def _copy_all(self, libs: list[str], src_dir_fn: Callable[[Path, str], Path]):
        for library_name in libs:
            self._copy_cpp_lib_files_if_any(library_name, src_dir_fn)

    def _copy_cpp_lib_files_if_any(
        self, library_name: str, src_dir_fn: Callable[[Path, str], Path]
    ):
        src_dir = src_dir_fn(self._site_packages_dir, library_name)
        dest_dir = calc_cpp_libs_dir(self._cpp_dir, library_name)
        if dest_dir.exists():
            shutil.rmtree(dest_dir)
        if src_dir.exists():
            shutil.copytree(src_dir, dest_dir)
