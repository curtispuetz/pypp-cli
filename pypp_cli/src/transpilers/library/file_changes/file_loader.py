from pathlib import Path


def calc_all_py_files(root: Path) -> list[Path]:
    ret: list[Path] = []
    for path in root.rglob("*.py"):
        r = path.relative_to(root)
        if r.parts[0] != ".venv":
            ret.append(r)
    return ret
