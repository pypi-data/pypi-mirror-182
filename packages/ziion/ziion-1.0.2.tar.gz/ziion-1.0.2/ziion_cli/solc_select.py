import os
from pathlib import Path
import urllib.request
import ziion_cli.utils
from ziion_cli.constants import (
    SOLC_SELECT_DIR,
    ARTIFACTS_DIR,
    S3_BUCKET_URL,
    SOLC_ARM_FOLDER_S3
)

def switch_global_version(version: str, always_install: bool) -> None:
    if version in installed_versions():
        with open(f"{SOLC_SELECT_DIR}/global-version", "w", encoding="utf-8") as f:
            f.write(version)
        print("Switched global version to", version)
    elif version in ziion_cli.utils.get_metadata_versions("solc"):
        if always_install:
            install_artifacts([version])
            switch_global_version(version, always_install)
        else:
            print(f"ziion-cli solc-select error: '{version}' must be installed prior to use.")
    else:
        print(f"ziion-cli solc-select error: Unknown version '{version}'")

def installed_versions() -> list[str]:
    try:
        return [
            f.replace("solc-", "") for f in sorted(os.listdir(ARTIFACTS_DIR)) if f.startswith("solc-")    
        ]
    except FileNotFoundError as e:
        return []

def install_artifacts(versions: list[str]) -> bool:
    #releases = utils.get_metadata_versions("solc")

    for version in versions:
        if "all" not in versions:
            if versions and version not in versions:
                continue

        url = S3_BUCKET_URL + SOLC_ARM_FOLDER_S3 + "solc-v" + version
        print(f"Installing '{version}'...")
        try:      
            urllib.request.urlretrieve(url, ARTIFACTS_DIR.joinpath(f"solc-{version}"))
        except urllib.error.HTTPError as e:     
            print(e.reason)
        
        with open(f"{SOLC_SELECT_DIR}/global-version", "w+", encoding="utf-8") as f:
            f.write(version)

        #verify_checksum(version)

        Path.chmod(ARTIFACTS_DIR.joinpath(f"solc-{version}"), 0o775)
        print(f"Version '{version}' installed and configured as default.\n")

    return True