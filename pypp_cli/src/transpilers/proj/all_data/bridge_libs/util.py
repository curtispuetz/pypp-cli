from pathlib import Path


def calc_cpp_libs_dir(cpp_dir: Path, library_name: str) -> Path:
    # TODO: move this just to the paths dataclass
    return cpp_dir / "libs"


def calc_library_cpp_data_dir(site_packages_dir: Path, library_name: str) -> Path:
    return site_packages_dir / library_name / "pypp_data" / "cpp"
