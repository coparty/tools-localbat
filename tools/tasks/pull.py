from fabric import Connection
from ..helpers import config, connector

def do_pull(connection: Connection, name: str, root: str) -> None:
    print("=> pulling {} ...".format(name))

    with connection.cd(root):
        connection.run("git pull")

    print("=> ok!")

def run_pull(project: str) -> None:
    # Read the config from config file
    print("Reading config file ...")

    [ssh, pull] = config.from_pull()

    # Try to connect remote server
    print("Start connecting ...")

    connection = connector.connect(ssh)

    # Try to pull the project in remote server by selected project name
    print("Parsing project name ...")

    # If project is all, pull defined all projects
    if project.lower() == "all":
        for name, root in pull.items():
            do_pull(connection, name, root)

    # If project is specified, just pull by specified
    if project in pull.keys():
        do_pull(connection, project, pull[project])

    # Handle unknown project keywords
    if project not in pull.keys() and project.lower() != "all":
        print("=> unknown project: {}".format(project))
