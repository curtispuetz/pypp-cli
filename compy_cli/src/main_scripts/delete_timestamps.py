from compy_cli.src.pypp_dirs import PyppDirs


def pypp_delete_timestamps(dirs: PyppDirs):
    if not dirs.timestamps_file.exists():
        print("file_timestamps.json does not exist, nothing to remove")
    else:
        dirs.timestamps_file.unlink()
        print("file_timestamps.json removed")
