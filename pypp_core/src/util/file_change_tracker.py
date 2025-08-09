import os
import json
from dataclasses import dataclass
import fnmatch
from pathlib import Path

from pypp_core.src.config import PyppDirs, create_test_dir_pypp_dirs
from pypp_core.src.constants import SECRET_MAIN_FILE_DIR_PREFIX


def _get_all_files(root: str) -> list[str]:
    # Tested. Results: works.
    ret: list[str] = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(dirpath, filename)
                ret.append(os.path.relpath(full_path, root))
    return ret


def get_all_main_files(python_dir: str) -> list[str]:
    return [f for f in os.listdir(python_dir) if f.endswith(".py")]


def _get_all_main_files_with_special_name(python_dir: str) -> list[tuple[str, str]]:
    return [
        (f, SECRET_MAIN_FILE_DIR_PREFIX + f) for f in get_all_main_files(python_dir)
    ]


def _load_previous_timestamps(timestamps_file: str):
    if os.path.exists(timestamps_file):
        with open(timestamps_file, "r") as f:
            return json.load(f)
    return {}


def save_timestamps(timestamps, timestamps_file: str):
    with open(timestamps_file, "w") as f:
        json.dump(timestamps, f, indent=2)


@dataclass(frozen=True, slots=True)
class _PyFileChanges:
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


def _should_ignore_file(src_file_rel_path: str, ignore_src_files: list[str]) -> bool:
    s: str = Path(src_file_rel_path).as_posix()
    for pattern in ignore_src_files:
        if fnmatch.fnmatch(s, pattern):
            return True
    return False


def calc_py_file_changes(
    dirs: PyppDirs, ignore_src_files: list[str]
) -> tuple[_PyFileChanges, dict]:
    prev_timestamps = _load_previous_timestamps(dirs.timestamps_file)
    curr_timestamps = {}
    changed_files = []
    new_files = []
    deleted_files = set(prev_timestamps.keys())
    ignored_src_files = 0

    for rel_path in _get_all_files(dirs.python_src_dir):
        abs_path = os.path.join(dirs.python_src_dir, rel_path)
        if not _should_ignore_file(rel_path, ignore_src_files):
            _check_file_change(
                abs_path,
                rel_path,
                curr_timestamps,
                prev_timestamps,
                changed_files,
                new_files,
                deleted_files,
            )
        else:
            ignored_src_files += 1
    for rel_path, secret_name in _get_all_main_files_with_special_name(dirs.python_dir):
        _check_file_change(
            os.path.join(dirs.python_dir, rel_path),
            secret_name,
            curr_timestamps,
            prev_timestamps,
            changed_files,
            new_files,
            deleted_files,
        )

    if not (changed_files or new_files or deleted_files):
        print("No file changes detected.")
    else:
        print(
            f"changed files: {len(changed_files)}, "
            f"new files: {len(new_files)}, "
            f"deleted files: {len(deleted_files)},"
            f" ignored src files: {ignored_src_files}"
        )

    return _PyFileChanges(
        changed_files, new_files, list(deleted_files)
    ), curr_timestamps


if __name__ == "__main__":
    calc_py_file_changes(create_test_dir_pypp_dirs())
