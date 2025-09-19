from pathlib import Path
import shutil


def rm_dirs_and_files(directory: Path, exclude_dir: set[str]) -> None:
    for path in directory.iterdir():
        if path.is_dir():
            if path.name not in exclude_dir:
                shutil.rmtree(path)
        elif path.is_file():
            path.unlink()
