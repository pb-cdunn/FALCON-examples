run: setup
	echo fc_run.py fc_run.cfg
setup:
	${MAKE} -C data ecoli
.PHONY: default run setup
