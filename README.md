# Tools LocalBat

A tool for managing the projects from the local to the remote server

## Installation

Create the virtual environment first

    python3 -m venv venv3

Activate the virtual environment

    source venv3/bin/activate

Upgrade the pip tools

    pip install -U pip

Install the required packages

    pip install -r requirements.txt

Create the default ssh and backup config

    cp configs/default.py.example configs/default.py
    cp configs/backup.py.example configs/backup.py

Open and edit those configs

    vim configs/default.py
    vim configs/backup.py

## Usage

### Activated virtual environment

List available tasks

    fab -l

Backup the remote projects to local download directory base on configuration file

    fab backup

### Deactivated virtual development

If you don't want to activate virtualenv, just want to quickly run the command, you can do it like:

    ./venv3/bin/fab backup

Or, you can simply using the following command defined in Makefile

    make backup

When all action is done, you can checkout the backup file

    ls -la ./download
