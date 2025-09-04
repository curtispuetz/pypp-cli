from pathlib import Path
import subprocess


def pypp_build(cpp_dir: Path):
    print("running cmake build...")
    # NOTE: you only need to do the first 'cmake -S . -B build' part if there was file
    #  changes to the code base. However, for simplicity, I will just do it each time.
    # cmake -S . -B build
    subprocess.run(["cmake", "-S", ".", "-B", "build"], cwd=cpp_dir, check=True)
    # cmake --build build --config Release
    subprocess.run(
        ["cmake", "--build", "build", "--config", "Release"],
        cwd=cpp_dir,
        check=True,
    )
    print("cmake build finished")
