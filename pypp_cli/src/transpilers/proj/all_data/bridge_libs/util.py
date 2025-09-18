from pathlib import Path


def calc_library_cpp_data_dir(site_packages_dir: Path, library_name: str) -> Path:
    return site_packages_dir / library_name / "pypp_data" / "cpp"
