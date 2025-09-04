from pathlib import Path
from pypp_cli.src.other.pypp_paths.delete_timestamps import create_timestamps_file


def pypp_delete_timestamps(target_dir: Path):
    timestamps_file = create_timestamps_file(target_dir)
    if not timestamps_file.exists():
        print("file_timestamps.json does not exist, nothing to remove")
    else:
        timestamps_file.unlink()
        print("file_timestamps.json removed")
