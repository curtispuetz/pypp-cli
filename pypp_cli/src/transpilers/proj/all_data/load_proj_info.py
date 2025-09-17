import json
from pathlib import Path

from pydantic import ValidationError

from pypp_cli.src.config import ProjInfo, ProjMetadata


def load_proj_info(proj_info_file: Path) -> ProjInfo:
    with open(proj_info_file) as file:
        proj_info = json.load(file)
    try:
        return ProjInfo(**proj_info)
    except ValidationError as e:
        raise ValueError(f"Issue found in proj_info.json file: {e}") from e


def load_metadata(metadata_file: Path) -> ProjMetadata:
    with open(metadata_file) as file:
        metadata = json.load(file)
    try:
        return ProjMetadata(**metadata)
    except ValidationError as e:
        raise ValueError(f"Issue found in metadata.json file: {e}") from e
