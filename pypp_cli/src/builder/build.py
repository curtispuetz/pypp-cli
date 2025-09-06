from pathlib import Path
import subprocess


def pypp_build(cpp_dir: Path):
    print("running cmake build...")
    # NOTE: you only need to do the first 'cmake -S . -B build' part if there was file
    #  changes to the code base. However, for simplicity, I will just do it each time.
    # cmake -S . -B build
    subprocess.check_call(["cmake", "-S", ".", "-B", "build"], cwd=cpp_dir)
    # cmake --build build --config Release
    subprocess.check_call(
        ["cmake", "--build", "build", "--config", "Release"],
        cwd=cpp_dir,
    )
    print("cmake build finished")
