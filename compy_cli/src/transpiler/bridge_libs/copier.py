from dataclasses import dataclass
from pathlib import Path
import shutil

from compy_cli.src.transpiler.bridge_libs.util import (
    calc_cpp_libs_dir,
    calc_library_cpp_data_dir,
)


def copy_all_bridge_lib_cpp_files(
    cpp_dir: Path, site_packages_dir: Path, bridge_libs_not_copied: list[str]
):
    copier = _CppBridgeLibCopier(cpp_dir, site_packages_dir)
    copier.copy_all(bridge_libs_not_copied)


@dataclass(frozen=True, slots=True)
class _CppBridgeLibCopier:
    _cpp_dir: Path
    _site_packages_dir: Path

    def copy_all(self, bridge_libs_not_copied: list[str]):
        for library_name in bridge_libs_not_copied:
            self._copy_cpp_lib_files_if_any(library_name)

    def _copy_cpp_lib_files_if_any(self, library_name: str):
        src_dir = calc_library_cpp_data_dir(self._site_packages_dir, library_name)
        dest_dir = calc_cpp_libs_dir(self._cpp_dir, library_name)
        if dest_dir.exists():
            shutil.rmtree(dest_dir)
        if src_dir.exists():
            shutil.copytree(src_dir, dest_dir)
