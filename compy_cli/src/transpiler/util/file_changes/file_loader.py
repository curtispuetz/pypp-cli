import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class TimeStampsFile:
    main_files: dict[str, float]
    src_files: dict[str, float]


def calc_all_py_files(root: Path) -> list[Path]:
    ret: list[Path] = []
    for path in root.rglob("*.py"):
        ret.append(path.relative_to(root))
    return ret


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
    return TimeStampsFile(
        main_files={},
        src_files={},
    )


class TimestampsSaver:
    def __init__(self, timestamps_file: Path):
        self._timestamps_file = timestamps_file

    def save(self, timestamps: TimeStampsFile):
        with open(self._timestamps_file, "w") as f:
            json.dump(
                {
                    "main_files": timestamps.main_files,
                    "src_files": timestamps.src_files,
                },
                f,
                indent=2,
            )
