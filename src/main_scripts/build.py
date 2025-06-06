import subprocess

from src.config import C_CPP_DIR


def pypp_build():
    # NOTE: you only need to do the first 'cmake -S . -B build' part if there was file
    #  changes to the code base. However, for simplicity, I will just do it each time.
    # cmake -S . -B build
    subprocess.run(["cmake", "-S", ".", "-B", "build"], cwd=C_CPP_DIR, check=True)
    # cmake --build build --config Release
    subprocess.run(
        ["cmake", "--build", "build", "--config", "Release"], cwd=C_CPP_DIR, check=True
    )
    print("py++ build finished")


if __name__ == "__main__":
    pypp_build()
