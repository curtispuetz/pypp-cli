import json
from dataclasses import dataclass
import fnmatch
from pathlib import Path

from pypp_core.src.config import PyppDirs, create_test_dir_pypp_dirs
from pypp_core.src.constants import SECRET_MAIN_FILE_DIR_PREFIX


def get_all_py_files(root: Path) -> list[Path]:
    ret: list[Path] = []
    for path in root.rglob("*.py"):
        ret.append(path.relative_to(root))
    return ret


def get_all_main_py_files(python_dir: Path) -> list[Path]:
    return [f for f in python_dir.glob("*.py") if f.is_file()]


def _get_main_files_special_names(main_py_files: list[Path]) -> list[Path]:
    return [Path(SECRET_MAIN_FILE_DIR_PREFIX + f.name) for f in main_py_files]


def _load_previous_timestamps(timestamps_file: Path) -> dict[str, float]:
    if timestamps_file.exists():
        with open(timestamps_file, "r") as f:
            return json.load(f)
    return {}


def save_timestamps(timestamps: dict[str, float], timestamps_file: Path):
    with open(timestamps_file, "w") as f:
        json.dump(timestamps, f, indent=2)


@dataclass(frozen=True, slots=True)
class _PyFileChanges:
    changed_files: list[Path]
    new_files: list[Path]
    deleted_files: list[Path]


def _check_file_change(
    filepath: Path,
    rel_path: Path,
    rel_path_posix: str,
    curr_timestamps: dict[str, float],
    prev_timestamps: dict[str, float],
    changed_files: list[Path],
    new_files: list[Path],
    deleted_files: set[Path],
):
    mtime = filepath.stat().st_mtime
    curr_timestamps[rel_path_posix] = mtime
    if rel_path_posix in prev_timestamps:
        deleted_files.discard(rel_path)
        if prev_timestamps[rel_path_posix] != mtime:
            changed_files.append(rel_path)
    else:
        new_files.append(rel_path)


def _should_ignore_file(rel_path_posix: str, ignore_src_files: list[str]) -> bool:
    for pattern in ignore_src_files:
        if fnmatch.fnmatch(rel_path_posix, pattern):
            return True
    return False


def calc_py_file_changes(
    dirs: PyppDirs,
    ignore_src_files: list[str],
    main_py_files: list[Path],
    src_py_files: list[Path],
) -> tuple[_PyFileChanges, dict[str, float]]:
    prev_timestamps: dict[str, float] = _load_previous_timestamps(dirs.timestamps_file)
    curr_timestamps: dict[str, float] = {}
    changed_files: list[Path] = []
    new_files: list[Path] = []
    deleted_files: set[Path] = {Path(k) for k in prev_timestamps.keys()}
    ignored_src_files = 0

    for rel_path in src_py_files:
        abs_path: Path = dirs.python_src_dir / rel_path
        rel_path_posix: str = rel_path.as_posix()
        if not _should_ignore_file(rel_path_posix, ignore_src_files):
            _check_file_change(
                abs_path,
                rel_path,
                rel_path_posix,
                curr_timestamps,
                prev_timestamps,
                changed_files,
                new_files,
                deleted_files,
            )
        else:
            ignored_src_files += 1
    secret_names = _get_main_files_special_names(main_py_files)
    for abs_path, rel_path in zip(main_py_files, secret_names):
        _check_file_change(
            abs_path,
            rel_path,
            rel_path.as_posix(),
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
    pypp_dirs = create_test_dir_pypp_dirs()
    calc_py_file_changes(
        pypp_dirs,
        [],
        get_all_main_py_files(pypp_dirs.python_dir),
        get_all_py_files(pypp_dirs.python_src_dir),
    )
