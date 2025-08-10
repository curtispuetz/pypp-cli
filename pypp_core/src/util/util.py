import os

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
