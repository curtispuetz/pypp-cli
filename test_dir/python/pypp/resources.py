import os


def pypp_get_resources(relative_path: str) -> str:
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, "..", "..", "resources", relative_path)