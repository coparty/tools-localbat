import json
import sys
from os import path

def from_file() -> list:
    config_path = path.abspath(path.join(path.dirname(__file__), "../../configs/backup.json"))
    config_data = json.load(open(config_path))

    ssh      = config_data["ssh"]
    backup   = config_data["backup"]
    download = config_data["download"]

    return [ssh, backup, download]
