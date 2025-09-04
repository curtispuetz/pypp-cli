from pathlib import Path


def calc_proj_info_path(proj_dir: Path) -> Path:
    return proj_dir / "pypp_files" / "proj_info.json"
