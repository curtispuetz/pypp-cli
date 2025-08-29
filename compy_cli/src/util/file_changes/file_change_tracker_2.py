from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
from compy_cli.src.compy_dirs import CompyDirs


@dataclass(frozen=True, slots=True)
class PyFileChanges2:
    changed_files: list[Path]
    new_files: list[Path]
    deleted_files: list[Path]
    ignored_file_stems: set[str]
    new_timestamps: dict[str, float]


def _should_ignore_file(rel_path_posix: str, ignore_src_files: list[str]) -> bool:
    for pattern in ignore_src_files:
        if fnmatch(rel_path_posix, pattern):
            return True
    return False


class FileChangeTracker:
    def __init__(self, prev_timestamps: dict[str, float]):
        self._prev_timestamps = prev_timestamps
        self._curr_timestamps: dict[str, float] = {}
        self._changed_files: list[Path] = []
        self._new_files: list[Path] = []
        self._deleted_files: set[Path] = self._find_deleted_files()
        self._ignored_file_stems: set[str] = set()

    def _find_deleted_files(self) -> set[Path]:
        if len(self._prev_timestamps) == 0:
            return set()
        return {Path(k) for k in list(self._prev_timestamps.keys())}

    def _check_file_change(self, filepath: Path, rel_path: Path, rel_path_posix: str):
        mtime = filepath.stat().st_mtime
        self._curr_timestamps[rel_path_posix] = mtime
        if rel_path_posix in self._prev_timestamps:
            self._deleted_files.discard(rel_path)
            if self._prev_timestamps[rel_path_posix] != mtime:
                self._changed_files.append(rel_path)
        else:
            self._new_files.append(rel_path)

    def calc_py_file_changes(
        self, root_dir: Path, ignore_files: list[str], py_files: list[Path]
    ) -> PyFileChanges2:
        for rel_path in py_files:
            abs_path: Path = root_dir / rel_path
            rel_path_posix: str = rel_path.as_posix()
            if not _should_ignore_file(rel_path_posix, ignore_files):
                self._check_file_change(abs_path, rel_path, rel_path_posix)
            else:
                self._ignored_file_stems.add(abs_path.stem)
        return PyFileChanges2(
            self._changed_files,
            self._new_files,
            list(self._deleted_files),
            self._ignored_file_stems,
            self._curr_timestamps,
        )
