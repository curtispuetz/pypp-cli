from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.package_manager.installer.json_verifier import (
    verify_bridge_json_files,
)


def verify_all_bridge_libs(
    bridge_libs_not_copied: list[str], bridge_json_path_cltr: BridgeJsonPathCltr
):
    for bridge_lib in bridge_libs_not_copied:
        verify_bridge_json_files(bridge_json_path_cltr, bridge_lib)
