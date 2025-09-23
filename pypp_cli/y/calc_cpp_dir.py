from pathlib import Path
from pypp_cli.y.proj_info import ProjInfo


def calc_cpp_dir(proj_info: ProjInfo, target_dir: Path) -> Path:
    if proj_info.override_cpp_write_dir is None:
        return target_dir / ".pypp" / "cpp"
    return target_dir / proj_info.override_cpp_write_dir
