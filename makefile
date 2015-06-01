run-ecoli: setup-ecoli
run-ecoli2: setup-ecoli
run-lambda: setup-lambda
run-%: #setup-%
	fc_run.py fc_run_$*.cfg logging.ini
setup-%:
	${MAKE} -C data $*

.PHONY: default run-% setup-%
