from pathlib import Path

from src.config import C_CPP_SRC_DIR, C_CPP_MAIN_FILE, C_CPP_DIR


def calc_cpp_and_h_files_to_format() -> list[Path]:
    # TODO: only format the modified files. Just like I only transpile the modified
    #  files.
    ret = [Path(C_CPP_MAIN_FILE).relative_to(C_CPP_DIR)]
    root_dir = Path(C_CPP_SRC_DIR)
    for cpp_file in root_dir.rglob("*.cpp"):
        ret.append(cpp_file.relative_to(C_CPP_DIR))
    for h_file in root_dir.rglob("*.h"):
        ret.append(h_file.relative_to(C_CPP_DIR))
    return ret
