from compy_cli.src.transpilers.other.transpiler.results import TranspileResults


def print_transpilation_results(r: TranspileResults, files_deleted: int):
    print(
        f"Compy transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: "
        f"{r.py_files_transpiled}, "
        f"header files written: "
        f"{r.h_files_written},"
        f" cpp files written: "
        f"{r.cpp_files_written}"
    )


def print_files_changed_results(
    changed_files: int, new_files: int, deleted_files: int, ignored_files: list[str]
):
    print(
        f"Analysed file changes. changed files: {changed_files}, "
        f"new files: {new_files}, "
        f"deleted files: {deleted_files}, "
        f"ignored files: {ignored_files}"
    )
