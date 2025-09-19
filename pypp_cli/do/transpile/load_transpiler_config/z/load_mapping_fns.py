from pathlib import Path

from pypp_cli.do.transpile.y.transpiler_config_models import MappingFunctions


def load_mapping_functions(mapping_fn_dir: Path) -> MappingFunctions:
    ret = {}
    if mapping_fn_dir.exists():
        for p in mapping_fn_dir.rglob("*.py"):
            with open(p, "r") as f:
                ret[p.relative_to(mapping_fn_dir).as_posix()] = f.read()
    return ret
