all:
	@echo
	@echo "Command      : Description"
	@echo "------------ : ------------"
	@echo "make backup  : Download the backup file from remote server"
	@echo "make pull    : Pull the remote project by ran git pull"
	@echo "make restart : Restart the remote project (on traefik config)"
	@echo

backup:
	@./venv3/bin/fab backup

# make pull project=<alias|all>
pull:
	@./venv3/bin/fab pull -p $(project)

# make restart project=<alias|all>
restart:
	@./venv3/bin/fab restart -p $(project)
