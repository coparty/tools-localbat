from fabric import Connection

def connect(ssh: dict) -> Connection:
    connection = None

    if ssh["mode"] == "ssh_config":
        connection = Connection(ssh["host"])
    else:
        connection = Connection(
            host=ssh["host"],
            user=ssh["user"],
            port=ssh["port"],
            connect_kwargs={
                "key_filename": ssh["key"]
            }
        )

    return connection
