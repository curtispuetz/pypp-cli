import json
from dataclasses import dataclass, asdict
from pathlib import Path

from pypp_cli.do.transpile.z.py_file_tracker import PyFilesTracker


@dataclass(frozen=True, slots=True)
class TimeStampsFile:
    main_files: list[str]
    timestamps: dict[str, float]


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
