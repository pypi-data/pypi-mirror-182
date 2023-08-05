import ziion_cli.cargo
import ziion_cli.solc_select
import ziion_cli.utils
from ziion_cli.constants import (
    SOLC_SELECT_DIR
)

def update_packages(metapackage, dryrun):
    match metapackage:
        case "cargo":
            s3_packages_list = ziion_cli.utils.get_metadata_versions(metapackage)
            local_packages_list = ziion_cli.cargo.installed_versions()
            if dryrun:
                ziion_cli.cargo.list_packages_to_be_updated(s3_packages_list, local_packages_list)
            else:
                ziion_cli.cargo.update_necessary_packages(s3_packages_list, local_packages_list)
        case "solc":
            s3_packages_list = ziion_cli.utils.get_metadata_versions(metapackage)
            local_packages_list = ziion_cli.solc_select.installed_versions()
            missing_artifacts = []
            for i in s3_packages_list:
                if i not in local_packages_list:
                    missing_artifacts.append(i)
            if dryrun:
                print("These versions can be installed: ")
                for version in missing_artifacts:
                    print("- " + version)
            elif not dryrun and missing_artifacts != []:
                ziion_cli.solc_select.install_artifacts(missing_artifacts)
            else:
                print("Solc artifacts are up to date!")

def solc_select_imp(version, install='False' ):
    ziion_cli.solc_select.switch_global_version(version, install)

def solc_select_get_versions(): 
    try:
        with open(f"{SOLC_SELECT_DIR}/global-version", "r", encoding="utf-8") as f:
            current_version = f.read()
        for i in ziion_cli.solc_select.installed_versions():
            if current_version == i:
                print(i + " (current, set by " + str(SOLC_SELECT_DIR) + "/global-version)")
            else:
                print(i)
    except FileNotFoundError as e:
        print("No solc version selected for current usage. Use ziion solc-select [Version] first.")

def update_cli():
    ziion_cli.utils.self_update()
