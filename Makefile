all:
	@echo
	@echo "Command     : Description"
	@echo "----------- : ------------"
	@echo "make backup : Download the backup file from remote server"
	@echo "make pull   : Pull the remote project by ran git pull"
	@echo

backup:
	@./venv3/bin/fab backup

# make pull project=<alias|all>
pull:
	@./venv3/bin/fab pull -p $(project)
