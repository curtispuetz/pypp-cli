from dataclasses import dataclass, field
from fnmatch import fnmatch
from pathlib import Path


@dataclass(frozen=True, slots=True)
class PyFileChanges:
    changed_files: list[Path]
    new_files: list[Path]
    deleted_files: list[Path]
    ignored_file_stems: set[str]
    new_timestamps: dict[str, float]

    def print_results(self):
        print(
            f"Analysed file changes. changed files: {len(self.changed_files)}, "
            f"new files: {len(self.new_files)}, "
            f"deleted files: {len(self.deleted_files)}, "
            f"ignored files: {list(self.ignored_file_stems)}"
        )


def calc_py_file_changes(
    prev_timestamps: dict[str, float],
    root_dir: Path,
    ignored_files: list[str],
    py_files: list[Path],
) -> PyFileChanges:
    fct = _FileChangeTracker(prev_timestamps, _find_deleted_files(prev_timestamps))
    return fct.calc_py_file_changes(root_dir, ignored_files, py_files)


def _should_ignore_file(rel_path_posix: str, ignored_files: list[str]) -> bool:
    for pattern in ignored_files:
        if fnmatch(rel_path_posix, pattern):
            return True
    return False


def _find_deleted_files(prev_timestamps) -> set[Path]:
    if len(prev_timestamps) == 0:
        return set()
    return {Path(k) for k in list(prev_timestamps.keys())}


@dataclass(frozen=True, slots=True)
class _FileChangeTracker:
    _prev_timestamps: dict[str, float]
    _deleted_files: set[Path]
    _curr_timestamps: dict[str, float] = field(default_factory=dict)
    _changed_files: list[Path] = field(default_factory=list)
    _new_files: list[Path] = field(default_factory=list)
    _ignored_file_stems: set[str] = field(default_factory=set)

    def _check_file_change(self, filepath: Path, rel_path: Path, rel_path_posix: str):
        modified_time = filepath.stat().st_mtime
        self._curr_timestamps[rel_path_posix] = modified_time
        if rel_path_posix in self._prev_timestamps:
            self._deleted_files.discard(rel_path)
            if self._prev_timestamps[rel_path_posix] != modified_time:
                self._changed_files.append(rel_path)
        else:
            self._new_files.append(rel_path)

    def calc_py_file_changes(
        self, root_dir: Path, ignored_files: list[str], py_files: list[Path]
    ) -> PyFileChanges:
        for rel_path in py_files:
            abs_path: Path = root_dir / rel_path
            rel_path_posix: str = rel_path.as_posix()
            if not _should_ignore_file(rel_path_posix, ignored_files):
                self._check_file_change(abs_path, rel_path, rel_path_posix)
            else:
                self._ignored_file_stems.add(abs_path.stem)
        return PyFileChanges(
            self._changed_files,
            self._new_files,
            list(self._deleted_files),
            self._ignored_file_stems,
            self._curr_timestamps,
        )
