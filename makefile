default:
	@echo 'Try "make run-foo" for any sub-dir of run/.'
run-%: setup-%
	cd run/$*; fc_run.py fc_run.cfg logging.ini
setup-%:
	git-sym update run/$*

.PHONY: default
