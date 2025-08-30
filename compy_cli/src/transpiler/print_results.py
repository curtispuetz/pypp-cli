from compy_cli.src.transpiler.util.transpiler import TranspileResults


def print_transpilation_results(r: TranspileResults, files_deleted: int):
    print(
        f"Compy transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: "
        f"{r.py_files_transpiled}, "
        f"header files written: "
        f"{r.header_files_written},"
        f" cpp files written: "
        f"{r.cpp_files_written}"
    )
