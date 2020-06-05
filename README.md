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
    cp configs/pull.py.example configs/pull.py

Open and edit those configs

    vim configs/default.py
    vim configs/backup.py
    vim configs/pull.py

## Usage

In the virtual environment, you have `fab` command to easy fire the tasks

- Show the available tasks

        fab -l

- Backup remote projects to local directory

        fab backup

- Pull the project source from git repository

    > The alias name was defined in the `pull` config file

        fab pull project=<alias|all>

If you don't want to activate the virtual environment, you also can do it like

- Usage

        ./venv3/bin/fab <task> [options]

- E.g. run the `backup` task in normal environment

        ./venv3/bin/fab backup

And, If you just want more simply, just using the `make` command

- Like

        make backup
        make pull project=<alias|all>
