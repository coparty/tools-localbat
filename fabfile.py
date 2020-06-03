#!/usr/bin/python

from fabric import task
from tools.tasks.backup import run_backup
from tools.tasks.pull import run_pull
from tools.tasks.restart import run_restart

@task
def backup(c):
    run_backup()

@task
def pull(c, project):
    run_pull(project)

@task
def restart(c, project):
    run_restart(project)
