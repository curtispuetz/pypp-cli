def print_files_changed_results(
    changed_files: int, new_files: int, deleted_files: int, ignored_files: list[str]
):
    print(
        f"Analysed file changes. changed files: {changed_files}, "
        f"new files: {new_files}, "
        f"deleted files: {deleted_files}, "
        f"ignored files: {ignored_files}"
    )
