import os
import subprocess
from functools import partial
from multiprocessing import Pool
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs


def _format_file(file: Path, dirs: CompyDirs):
    # clang-format -i --style=file main.cpp
    subprocess.run(
        ["clang-format", "-i", "--style=file", str(file)], cwd=dirs.cpp_dir, check=True
    )


def compy_format(files_added_or_modified: list[Path], dirs: CompyDirs):
    num_cores = os.cpu_count() or 1  # Fallback to 1 if None
    with Pool(num_cores) as p:  # Adjust number of workers
        p.map(partial(_format_file, dirs=dirs), files_added_or_modified)
    print(
        f"Compy format finished. "
        f"files formatted: {len(files_added_or_modified)}, "
        f"cores used: {num_cores}"
    )
