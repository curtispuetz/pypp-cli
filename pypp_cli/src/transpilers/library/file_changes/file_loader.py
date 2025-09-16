from pathlib import Path


def calc_all_py_files(root: Path) -> list[Path]:
    ret: list[Path] = []
    for path in root.iterdir():
        if path.name == ".venv":
            continue
        if path.is_dir():
            for p in path.rglob("*.py"):
                ret.append(p.relative_to(root))
        if path.is_file() and path.suffix == ".py":
            ret.append(path.relative_to(root))
    return ret
