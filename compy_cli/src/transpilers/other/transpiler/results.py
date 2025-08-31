from dataclasses import dataclass
from pathlib import Path


@dataclass
class TranspileResults:
    files_added_or_modified: list[Path]
    py_files_transpiled: int
    h_files_written: int
    cpp_files_written: int
