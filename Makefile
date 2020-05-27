all:
	@echo
	@echo "Command     : Description"
	@echo "----------- : ------------"
	@echo "make backup : Download the backup file from remote server"
	@echo

backup:
	@./venv3/bin/python3 index.py
