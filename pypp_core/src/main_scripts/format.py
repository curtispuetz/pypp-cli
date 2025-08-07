import os
import subprocess
from multiprocessing import Pool
from pathlib import Path

from pypp_core.src.config import C_CPP_DIR


def _format_file(file: Path):
    # clang-format -i --style=file main.cpp
    subprocess.run(
        ["clang-format", "-i", "--style=file", str(file)], cwd=C_CPP_DIR, check=True
    )


def pypp_format(files_added_or_modified: list[Path]):
    num_cores = os.cpu_count() or 1  # Fallback to 1 if None
    with Pool(num_cores) as p:  # Adjust number of workers
        p.map(_format_file, files_added_or_modified)
    print(
        f"py++ format finished. "
        f"files formatted: {len(files_added_or_modified)}, "
        f"cores used: {num_cores}"
    )


if __name__ == "__main__":
    pypp_format([])
