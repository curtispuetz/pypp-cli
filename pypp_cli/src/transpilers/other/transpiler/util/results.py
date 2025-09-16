from dataclasses import dataclass
from pathlib import Path


@dataclass
class TranspileResults:
    files_added_or_modified: list[Path]
    py_files_transpiled: int
    h_files_written: int
    cpp_files_written: int

    def print(self, files_deleted: int):
        print(
            f"Py++ transpile finished. "
            f"py files transpiled: "
            f"{self.py_files_transpiled}, "
            f"header files written: "
            f"{self.h_files_written},"
            f" cpp files written: "
            f"{self.cpp_files_written}, "
            f"header and cpp files deleted: {files_deleted}"
        )
