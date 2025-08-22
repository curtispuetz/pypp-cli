import json
from dataclasses import dataclass
import fnmatch
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs, create_test_dir_compy_dirs


@dataclass(frozen=True, slots=True)
class PyChangedFile:
    rel_path: Path
    is_main_file: bool


@dataclass(frozen=True, slots=True)
class PyFileChanges:
    changed_files: list[PyChangedFile]
    new_files: list[PyChangedFile]
    deleted_files: list[Path]


type TimeStampsFile = dict[str, dict[str, float]]


def get_all_py_files(root: Path) -> list[Path]:
    ret: list[Path] = []
    for path in root.rglob("*.py"):
        ret.append(path.relative_to(root))
    return ret


def get_all_main_py_files(python_dir: Path) -> list[Path]:
    ret: list[Path] = []
    for path in python_dir.glob("*.py"):
        if path.is_file():
            ret.append(path.relative_to(python_dir))
    return ret


def _load_previous_timestamps(timestamps_file: Path) -> TimeStampsFile:
    if timestamps_file.exists():
        with open(timestamps_file, "r") as f:
            return json.load(f)
    return {
        "main_files": {},
        "src_files": {},
    }


def save_timestamps(timestamps: TimeStampsFile, timestamps_file: Path):
    with open(timestamps_file, "w") as f:
        json.dump(timestamps, f, indent=2)


def _check_file_change(
    is_main_file: bool,
    filepath: Path,
    rel_path: Path,
    rel_path_posix: str,
    curr_timestamps: TimeStampsFile,
    prev_timestamps: TimeStampsFile,
    changed_files: list[PyChangedFile],
    new_files: list[PyChangedFile],
    deleted_files: set[Path],
):
    file_type = "main_files" if is_main_file else "src_files"
    mtime = filepath.stat().st_mtime
    curr_timestamps[file_type][rel_path_posix] = mtime
    if rel_path_posix in prev_timestamps[file_type]:
        deleted_files.discard(rel_path)
        if prev_timestamps[file_type][rel_path_posix] != mtime:
            changed_files.append(PyChangedFile(rel_path, is_main_file))
    else:
        new_files.append(PyChangedFile(rel_path, is_main_file))


def _should_ignore_file(rel_path_posix: str, ignore_src_files: list[str]) -> bool:
    for pattern in ignore_src_files:
        if fnmatch.fnmatch(rel_path_posix, pattern):
            return True
    return False


def _find_deleted_files(prev_timestamps: TimeStampsFile) -> set[Path]:
    if len(prev_timestamps) == 0:
        return set()
    return {
        Path(k)
        for k in list(prev_timestamps["main_files"].keys())
        + list(prev_timestamps["src_files"].keys())
    }


def calc_py_file_changes(
    dirs: CompyDirs,
    ignore_src_files: list[str],
    main_py_files: list[Path],
    src_py_files: list[Path],
) -> tuple[PyFileChanges, TimeStampsFile]:
    prev_timestamps: TimeStampsFile = _load_previous_timestamps(dirs.timestamps_file)
    curr_timestamps: TimeStampsFile = {
        "main_files": {},
        "src_files": {},
    }
    changed_files: list[PyChangedFile] = []
    new_files: list[PyChangedFile] = []
    deleted_files: set[Path] = _find_deleted_files(prev_timestamps)
    ignored_src_files = 0

    for rel_path in src_py_files:
        abs_path: Path = dirs.python_src_dir / rel_path
        rel_path_posix: str = rel_path.as_posix()
        if not _should_ignore_file(rel_path_posix, ignore_src_files):
            _check_file_change(
                False,
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
    for rel_path in main_py_files:
        abs_path: Path = dirs.python_dir / rel_path
        print("main file, ", rel_path)
        _check_file_change(
            True,
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

    return PyFileChanges(changed_files, new_files, list(deleted_files)), curr_timestamps


if __name__ == "__main__":
    compy_dirs = create_test_dir_compy_dirs()
    calc_py_file_changes(
        compy_dirs,
        [],
        get_all_main_py_files(compy_dirs.python_dir),
        get_all_py_files(compy_dirs.python_src_dir),
    )
