import json
from dataclasses import dataclass, asdict
from pathlib import Path

from pypp_cli.src.transpilers.other.other.file_tracker import PyFilesTracker


@dataclass(frozen=True, slots=True)
class TimeStampsFile:
    main_files: list[str]
    timestamps: dict[str, float]


def calc_all_main_py_files(python_dir: Path) -> list[Path]:
    ret: list[Path] = []
    for path in python_dir.glob("*.py"):
        if path.is_file():
            ret.append(path.relative_to(python_dir))
    return ret


def load_previous_timestamps(timestamps_file: Path) -> TimeStampsFile:
    if timestamps_file.exists():
        with open(timestamps_file, "r") as f:
            data = json.load(f)
        return TimeStampsFile(**data)
    return TimeStampsFile([], {})


@dataclass(frozen=True, slots=True)
class TimestampsSaver:
    _timestamps_file: Path
    _py_files_tracker: PyFilesTracker

    def save(self, timestamps: dict[str, float]):
        with open(self._timestamps_file, "w") as f:
            json.dump(
                asdict(
                    TimeStampsFile(
                        [str(f) for f in self._py_files_tracker.main_files], timestamps
                    )
                ),
                f,
                indent=2,
            )
