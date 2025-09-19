from pathlib import Path

from pypp_cli.do.transpile.find_libs.z.other.find_all_libs import (
    PyppLibsData,
    find_all_libs,
)
from pypp_cli.do.transpile.find_libs.z.other.find_new_libs import find_new_libs


def find_libs(site_packages_dir: Path, cpp_dir: Path) -> tuple[PyppLibsData, set[str]]:
    libs_data: PyppLibsData = find_all_libs(site_packages_dir)
    new_libs = find_new_libs(cpp_dir, libs_data.libs)
    return libs_data, new_libs
