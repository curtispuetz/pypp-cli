from compy_cli.src.dirs_cltr import CompyDirsCltr


def compy_delete_timestamps(dirs_cltr: CompyDirsCltr):
    timestamps_files = dirs_cltr.calc_timestamps_file()
    if not timestamps_files.exists():
        print("file_timestamps.json does not exist, nothing to remove")
    else:
        timestamps_files.unlink()
        print("file_timestamps.json removed")
