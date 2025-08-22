from compy_cli.src.compy_dirs import CompyDirs


def pypp_delete_timestamps(dirs: CompyDirs):
    if not dirs.timestamps_file.exists():
        print("file_timestamps.json does not exist, nothing to remove")
    else:
        dirs.timestamps_file.unlink()
        print("file_timestamps.json removed")
