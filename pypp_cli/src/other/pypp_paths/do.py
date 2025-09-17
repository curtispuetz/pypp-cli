from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.config import ProjInfo
from pypp_cli.src.other.pypp_paths.util import calc_sitepackages_dir
from pypp_cli.src.transpilers.proj.all_data.load_proj_info import load_proj_info


@dataclass(frozen=True, slots=True)
class DoPyppPaths:
    proj_info_file: Path
    cpp_dir: Path
    cpp_build_release_dir: Path
    python_dir: Path
    timestamps_file: Path
    site_packages_dir: Path


@dataclass(frozen=True, slots=True)
class DoTranspileDeps:
    paths: DoPyppPaths
    proj_info: ProjInfo


def create_do_pypp_paths(target_dir: Path) -> DoTranspileDeps:
    pypp_dir = target_dir / ".pypp"
    proj_info_file = pypp_dir / "proj_info.json"
    proj_info: ProjInfo = load_proj_info(proj_info_file)
    if proj_info.override_cpp_write_dir is None:
        cpp_dir = pypp_dir / "cpp"
    else:
        cpp_dir = target_dir / proj_info.override_cpp_write_dir
    cpp_build_release_dir = cpp_dir / "build"
    python_dir = target_dir
    timestamps_file = pypp_dir / "file_timestamps.json"
    site_packages_dir = calc_sitepackages_dir(python_dir)
    return DoTranspileDeps(
        DoPyppPaths(
            proj_info_file,
            cpp_dir,
            cpp_build_release_dir,
            python_dir,
            timestamps_file,
            site_packages_dir,
        ),
        proj_info,
    )
