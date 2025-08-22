from pathlib import Path
import shutil

from compy_cli.src.util.inner_strings import calc_inside_rd


def calc_ref_str(type_cpp: str) -> tuple[str, str]:
    if type_cpp.startswith("Ref(") and type_cpp.endswith(")"):
        return "&", calc_inside_rd(type_cpp)
    return "", type_cpp


def find_file_with_extension(directory: Path, extension: str) -> Path | None:
    for path in directory.iterdir():
        if path.is_file() and path.name.endswith(extension):
            return path
    return None


def rm_dirs_and_files(directory: Path, exclude_dir: set[str]) -> None:
    for path in directory.iterdir():
        if path.is_dir():
            if path.name not in exclude_dir:
                shutil.rmtree(path)
        elif path.is_file():
            path.unlink()
