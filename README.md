# Tools LocalBak

A tool for backup the projects from the remote server to the local directory

## Installation

Create the virtual environment first

    python3 -m venv venv3

Activate the virtual environment

    source venv3/bin/activate

Upgrade the pip tools

    pip install -U pip

Install the required packages

    pip install -r requirements.txt

Create the `config.json`

    cp config.json.example config.json

Open and edit the `config.json`

    vim config.json

## Usage

Run in the activated virtual environment

    python3 backup.py

Run in the deactivated virtual environment

    ./venv3/bin/python3 backup.py

Or, you can simply using the following command

    make backup

When all action is done, you can checkout the backup file

    ls -la ./download
