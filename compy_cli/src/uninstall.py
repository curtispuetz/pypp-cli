import subprocess


from compy_cli.src.dirs_cltr import CompyDirsCltr


def compy_uninstall(library: str, dirs_cltr: CompyDirsCltr):
    print(f"running 'pip uninstall {library}'...")
    subprocess.check_call(
        [dirs_cltr.calc_py_executable(), "-m", "pip", "uninstall", library]
    )
