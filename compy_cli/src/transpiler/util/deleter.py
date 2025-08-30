from pathlib import Path


# TODO: extract to common place
def delete_cpp_and_h_files(file_lists: list[list[Path]], cpp_src_dir: Path) -> int:
    files_deleted: int = 0
    for files in file_lists:
        for file in files:
            files_deleted += _delete_cpp_and_h_file(file, cpp_src_dir)
    return files_deleted


def _delete_cpp_and_h_file(filepath: Path, cpp_src_dir: Path) -> int:
    files_deleted: int = 0
    cpp_file: Path = filepath.with_suffix(".cpp")
    h_file: Path = filepath.with_suffix(".h")
    cpp_full_path: Path = cpp_src_dir / cpp_file
    h_full_path: Path = cpp_src_dir / h_file
    if cpp_full_path.exists():
        cpp_full_path.unlink()
        files_deleted += 1
    if h_full_path.exists():
        h_full_path.unlink()
        files_deleted += 1
    return files_deleted
