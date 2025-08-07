import os

from pypp_core.src.config import PyppDirs


def pypp_remove_timestamps(dirs: PyppDirs):
    if not os.path.exists(dirs.timestamps_file):
        print("file_timestamps.json does not exist, nothing to remove")
    else:
        os.remove(dirs.timestamps_file)
        print("file_timestamps.json removed")
