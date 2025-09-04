from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class CppAndHFileDeleter:
    _cpp_src_dir: Path

    def delete_files(self, file_lists: list[list[Path]]) -> int:
        files_deleted: int = 0
        for files in file_lists:
            for file in files:
                files_deleted += self._delete_cpp_and_h_file(file)
        return files_deleted

    def _delete_cpp_and_h_file(self, filepath: Path) -> int:
        files_deleted: int = 0
        cpp_file: Path = filepath.with_suffix(".cpp")
        h_file: Path = filepath.with_suffix(".h")
        cpp_full_path: Path = self._cpp_src_dir / cpp_file
        h_full_path: Path = self._cpp_src_dir / h_file
        if cpp_full_path.exists():
            cpp_full_path.unlink()
            files_deleted += 1
        if h_full_path.exists():
            h_full_path.unlink()
            files_deleted += 1
        return files_deleted
