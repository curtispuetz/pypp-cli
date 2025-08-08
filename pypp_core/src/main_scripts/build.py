import subprocess

from pypp_core.src.config import PyppDirs, create_test_dir_pypp_dirs


def pypp_build(dirs: PyppDirs):
    print("running cmake build...")
    # NOTE: you only need to do the first 'cmake -S . -B build' part if there was file
    #  changes to the code base. However, for simplicity, I will just do it each time.
    # cmake -S . -B build
    subprocess.run(["cmake", "-S", ".", "-B", "build"], cwd=dirs.cpp_dir, check=True)
    # cmake --build build --config Release
    subprocess.run(
        ["cmake", "--build", "build", "--config", "Release"],
        cwd=dirs.cpp_dir,
        check=True,
    )
    print("cmake build finished")


if __name__ == "__main__":
    pypp_build(create_test_dir_pypp_dirs())
