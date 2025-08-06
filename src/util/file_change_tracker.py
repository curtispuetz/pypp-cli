import os
import json
from dataclasses import dataclass

from src.config import C_PYTHON_SRC_DIR, C_TARGET_DIR, C_PYTHON_DIR
from src.constants import SECRET_MAIN_FILE_DIR_PREFIX

TIMESTAMPS_FILE = os.path.join(C_TARGET_DIR, "file_timestamps.json")


def get_all_files(root: str) -> list[str]:
    # Tested. Results: works.
    ret: list[str] = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(dirpath, filename)
                ret.append(os.path.relpath(full_path, root))
    return ret


def get_all_main_files() -> list[str]:
    return [f for f in os.listdir(C_PYTHON_DIR) if f.endswith(".py")]


def get_all_main_files_with_special_name() -> list[tuple[str, str]]:
    return [(f, SECRET_MAIN_FILE_DIR_PREFIX + f) for f in get_all_main_files()]


def load_previous_timestamps():
    if os.path.exists(TIMESTAMPS_FILE):
        with open(TIMESTAMPS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_timestamps(timestamps):
    with open(TIMESTAMPS_FILE, "w") as f:
        json.dump(timestamps, f, indent=2)


@dataclass(frozen=True, slots=True)
class PyFileChanges:
    changed_files: list[str]
    new_files: list[str]
    deleted_files: list[str]


def _check_file_change(
    filepath,
    rel_path,
    curr_timestamps,
    prev_timestamps,
    changed_files,
    new_files,
    deleted_files,
):
    mtime = os.path.getmtime(filepath)
    curr_timestamps[rel_path] = mtime
    if rel_path in prev_timestamps:
        deleted_files.discard(rel_path)
        if prev_timestamps[rel_path] != mtime:
            changed_files.append(rel_path)
    else:
        new_files.append(rel_path)


def calc_py_file_changes() -> tuple[PyFileChanges, dict]:
    prev_timestamps = load_previous_timestamps()
    curr_timestamps = {}
    changed_files = []
    new_files = []
    deleted_files = set(prev_timestamps.keys())

    for rel_path in get_all_files(C_PYTHON_SRC_DIR):
        _check_file_change(
            os.path.join(C_PYTHON_SRC_DIR, rel_path),
            rel_path,
            curr_timestamps,
            prev_timestamps,
            changed_files,
            new_files,
            deleted_files,
        )
    for rel_path, secret_name in get_all_main_files_with_special_name():
        _check_file_change(
            os.path.join(C_PYTHON_DIR, rel_path),
            secret_name,
            curr_timestamps,
            prev_timestamps,
            changed_files,
            new_files,
            deleted_files,
        )

    if not (changed_files or new_files or deleted_files):
        print("No changes detected.")
    else:
        print(
            f"changed files: {len(changed_files)}, "
            f"new files: {len(new_files)}, "
            f"deleted files: {len(deleted_files)}"
        )

    return PyFileChanges(changed_files, new_files, list(deleted_files)), curr_timestamps


if __name__ == "__main__":
    calc_py_file_changes()
