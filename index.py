#!/usr/bin/python

import os
import sys
from dotenv import load_dotenv
from fabric import Connection

def main():
    ssh_mode = os.getenv("SSH_MODE", "custom")
    ssh_host = os.getenv("SSH_HOST", None)
    ssh_port = os.getenv("SSH_PORT", None)
    ssh_user = os.getenv("SSH_USER", None)
    ssh_key  = os.getenv("SSH_KEY")

    c = None

    if ssh_mode == "ssh_config":
        c = Connection(ssh_host)
    else:
        c = Connection(ssh_host, user=ssh_user, port=ssh_port, connect_kwargs={
            "key_filename": ssh_key
        })

    c.run("pwd")
    c.run("uname -a")

if __name__ == "__main__":
    load_dotenv()
    main()
