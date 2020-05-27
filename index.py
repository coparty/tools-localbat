#!/usr/bin/python

import json
from os import path
from datetime import datetime, timezone, timedelta
from fabric import Connection

def local_time() -> datetime:
    tz = timezone(timedelta(hours=+8))

    return datetime.now(tz)

def main():
    # Read the config from config file
    print("Reading config file ...")

    config = json.load(open("./config.json"))

    ssh    = config["ssh"]
    backup = config["backup"]

    # Try to connect remote server
    print("Start connecting ...")

    c = None

    if ssh["mode"] == "ssh_config":
        c = Connection(ssh["host"])
    else:
        c = Connection(ssh["host"], user=ssh["user"], port=ssh["port"], connect_kwargs={
            "key_filename": ssh["key"]
        })

    # Loop projects
    print("Start backup projects ...")

    for project_name, project_path in backup["from"].items():
        print("=> {}".format(project_name))

        to_zip_path      = backup["to"][project_name]
        backup_directory = path.dirname(to_zip_path)

        backup_date = local_time().strftime("%Y%m%d")
        to_zip_path = to_zip_path.replace("{date}", backup_date)

        c.run("mkdir -p {}".format(backup_directory))
        c.run("tar zcPf {} {}".format(to_zip_path, project_path))

    print("finished!")

if __name__ == "__main__":
    main()
