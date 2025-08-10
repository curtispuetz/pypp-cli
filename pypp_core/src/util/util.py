import os
import shutil

from pypp_core.src.util.inner_strings import calc_inside_rd


def calc_ref_str(type_cpp: str) -> tuple[str, str]:
    if type_cpp.startswith("Ref(") and type_cpp.endswith(")"):
        return "&", calc_inside_rd(type_cpp)
    return "", type_cpp


def find_file_with_extension(directory: str, extension: str) -> str | None:
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            return os.path.join(directory, filename)
    return None


def rm_dirs_and_files(directory: str, exclude_dir: set[str]) -> None:
    for p in os.listdir(directory):
        f = os.path.join(directory, p)
        if os.path.isdir(f):
            if p not in exclude_dir:
                shutil.rmtree(f)
        if os.path.isfile(f):
            os.remove(f)
