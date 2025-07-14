import subprocess
from pathlib import Path

from src.config import C_CPP_BUILD_RELEASE_DIR


def pypp_run():
    exe_path = Path(C_CPP_BUILD_RELEASE_DIR) / "main.exe"
    print("py++ running executable...")
    subprocess.run([str(exe_path)], check=True)
    # TODO later: uncomment this print later maybe
    # print("py++ run finished")


if __name__ == "__main__":
    pypp_run()
