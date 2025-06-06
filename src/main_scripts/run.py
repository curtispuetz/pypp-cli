import subprocess
from pathlib import Path

from src.config import C_CPP_BUILD_RELEASE_DIR


def pypp_run():
    exe_path = Path(C_CPP_BUILD_RELEASE_DIR) / "pyppDefaultExeName.exe"
    print("py++ running executable...")
    subprocess.run([str(exe_path)], check=True)
    print("py++ run finished")


if __name__ == "__main__":
    pypp_run()
