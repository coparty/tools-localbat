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

    ssh      = config["ssh"]
    backup   = config["backup"]
    download = config["download"]

    # Try to connect remote server
    print("Start connecting ...")

    c = None

    if ssh["mode"] == "ssh_config":
        c = Connection(ssh["host"])
    else:
        c = Connection(ssh["host"], user=ssh["user"], port=ssh["port"], connect_kwargs={
            "key_filename": ssh["key"]
        })

    # Loop projects to backup
    print("Start backup projects ...")

    for project_name, project_path in backup["from"].items():
        print("=> {}".format(project_name))

        backup_date = local_time().strftime("%Y%m%d")
        to_zip_path = backup["to"][project_name].replace("{date}", backup_date)

        backup_directory = path.dirname(to_zip_path)
        backup_filename  = path.basename(to_zip_path)

        print("==> marking backup root directory")
        c.run("mkdir -p {}".format(backup_directory))

        print("==> compressing project to backup directory")
        c.run("tar zcPf {} {}".format(to_zip_path, project_path))

        print("==> sum the compressed file")
        command = c.run("md5sum {}".format(to_zip_path), hide=True)
        zip_md5 = command.stdout.split(" ")[0]

        if download["enable"]:
            print("==> downloading compressed file to local directory")

            download_path = path.realpath("{}/{}".format(download["path"], backup_filename))

            c.get(to_zip_path, download_path)

            command = c.local("md5sum {}".format(download_path), hide=True)
            local_zip_md5 = command.stdout.split(" ")[0]

            if zip_md5 == local_zip_md5:
                print("==> sum is match")
            else:
                print("==> sum is not match")

            if download["remove"]:
                print("==> removing compressed file")

                c.run("rm -f {}".format(to_zip_path))

    # Show finished
    print("finished!")

if __name__ == "__main__":
    main()
