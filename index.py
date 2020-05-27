#!/usr/bin/python

import os
from dotenv import load_dotenv
from fabric import Connection

def main():
    print(os.getenv("SSH_HOST"))
    print(os.getenv("SSH_PORT"))
    print(os.getenv("SSH_USER"))
    print(os.getenv("SSH_KEY"))
    pass

if __name__ == "__main__":
    load_dotenv()
    main()
