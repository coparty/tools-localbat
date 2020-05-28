from os import path
from fabric import Connection
from ..helpers import config, connector
from ..helpers.datetime import local_time

def do_download(connection: Connection, download: dict, backup_filename: str, remote_zip_path: str, remote_zip_md5: str) -> None:
    if download["enable"]:
        print("==> downloading compressed file to local directory")

        # Generate absolute download directory path for local
        download_path = path.realpath("{}/{}".format(download["path"], backup_filename))

        # Download remote compressed zip file to local download directory
        connection.get(remote_zip_path, download_path)

        # Compare the remote zip and local zip base on md5sum value
        command = connection.local("md5sum {}".format(download_path), hide=True)
        local_zip_md5 = command.stdout.split(" ")[0]

        if remote_zip_md5 == local_zip_md5:
            print("==> sum is match")
        else:
            print("==> sum is not match")

        # Remove the remote zip if remove is true
        if download["remove"]:
            print("==> removing compressed file")

            connection.run("rm -f {}".format(remote_zip_path))

def run_backup():
    # Read the config from config file
    print("Reading config file ...")

    [ssh, backup, download] = config.from_file()

    # Try to connect remote server
    print("Start connecting ...")

    connection = connector.connect(ssh)

    # Loop projects to backup
    print("Start backup projects ...")

    for project_name, project_path in backup["from"].items():
        print("=> {}".format(project_name))

        # Replace backup name from backup.{date}.tar.gz to backup.20200528.tar.gz
        backup_date = local_time().strftime("%Y%m%d")
        to_zip_path = backup["to"][project_name].replace("{date}", backup_date)

        # Get the backup directory, filename from target zip path
        # (e.g. /path/to/backup/project.{date}.tar.gz)
        # - directory: /path/to/backup
        # - filename : project.{date}.tar.gz
        backup_directory = path.dirname(to_zip_path)
        backup_filename  = path.basename(to_zip_path)

        # Create the backup directory,
        # Compress the project to backup directory
        # Sum the compressed file
        print("==> marking backup root directory")
        connection.run("mkdir -p {}".format(backup_directory))

        print("==> compressing project to backup directory")
        connection.run("tar zcPf {} {}".format(to_zip_path, project_path))

        print("==> sum the compressed file")
        command = connection.run("md5sum {}".format(to_zip_path), hide=True)
        zip_md5 = command.stdout.split(" ")[0]

        # Handle download action
        do_download(
            connection, download, backup_filename,
            remote_zip_path=to_zip_path,
            remote_zip_md5=zip_md5
        )

    print("Finished!")
