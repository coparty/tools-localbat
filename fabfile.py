#!/usr/bin/python

from fabric import task
from tools.tasks.backup import run_backup

@task
def backup(c):
    run_backup()
