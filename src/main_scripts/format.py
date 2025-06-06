import subprocess
from multiprocessing import Pool
from pathlib import Path

from src.config import C_CPP_DIR
from src.util.calc_src_files import calc_cpp_and_h_files_to_format


def _format_file(file: Path):
    subprocess.run(
        ["clang-format", "-i", "--style=file", str(file)], cwd=C_CPP_DIR, check=True
    )


def pypp_format():
    # clang-format -i --style=file main.cpp
    files = calc_cpp_and_h_files_to_format()
    with Pool(4) as p:  # Adjust number of workers
        p.map(_format_file, files)
    print("py++ format finished")


if __name__ == "__main__":
    pypp_format()
