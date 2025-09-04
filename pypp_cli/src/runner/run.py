import subprocess
from pathlib import Path


def pypp_run(cpp_build_release_dir: Path, exe_name: str | None):
    exe_path = cpp_build_release_dir / f"{exe_name}.exe"
    print("running generated executable...")
    subprocess.run([str(exe_path)], check=True)
    # TODO later: uncomment this print later maybe
    # print("Py++ run finished")
