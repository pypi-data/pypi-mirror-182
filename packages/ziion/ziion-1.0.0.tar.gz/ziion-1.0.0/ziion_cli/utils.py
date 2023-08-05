import subprocess
import re
import json
import platform

def parse_str_to_dict(s) -> (dict):
    packages = {}
    lines = s.splitlines()
    for line in lines:
        package_name = re.match("([^\s]+)",line)
        if package_name != None and package_name.group() != "Package":
            segments = line.split()
            packages[package_name.group()] = segments[1]
    return packages

def get_metadata_versions(metapackage="cargo") -> (dict):
    if metapackage == 'solc':
        s3_folder = "solc-arm-binaries/"
    elif metapackage == 'cargo':
        if platform.machine() == 'x86_64':
            s3_folder = "rust-amd-binaries/"
        elif platform.machine() == 'aarch64':
            s3_folder = "rust-arm-binaries/"
    subprocess.run(["wget", "-O", "metadata.json", "https://ziion-binaries.s3.amazonaws.com/"+ s3_folder + "metadata.json"], 
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT)
    f = open('metadata.json')
    data = json.load(f)
    return data["releases"]