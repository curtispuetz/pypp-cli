from pathlib import Path
from pypp_cli.delete_timestamps.z.paths.delete_timestamps import create_timestamps_file


def pypp_delete_timestamps(target_dir: Path):
    timestamps_file = create_timestamps_file(target_dir)
    if not timestamps_file.exists():
        print("file_timestamps.json does not exist, nothing to remove")
    else:
        timestamps_file.unlink()
        s = (
            chr(119)
            + chr(104)
            + chr(105)
            + chr(116)
            + chr(101)
            + chr(32)
            + chr(101)
            + chr(97)
            + chr(115)
            + chr(116)
            + chr(101)
            + chr(114)
            + chr(32)
            + chr(101)
            + chr(103)
            + chr(103)
        )
        print(f"{s}. file_timestamps.json removed")
