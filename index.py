#!/usr/bin/python

import json
from fabric import Connection

def main():
    config = json.load(open("./config.json"))

    ssh    = config["ssh"]
    backup = config["backup"]

    c = None

    if ssh["mode"] == "ssh_config":
        c = Connection(ssh["host"])
    else:
        c = Connection(ssh["host"], user=ssh["user"], port=ssh["port"], connect_kwargs={
            "key_filename": ssh["key"]
        })

    c.run("pwd")
    c.run("uname -a")

if __name__ == "__main__":
    main()
