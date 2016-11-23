default:
	@echo 'Try "make run-foo" for any sub-dir of run/.'
run-%: setup-%
	cd run/$*; fc_run.py fc_run.cfg logging.ini
setup-%:
	git-sym update run/$*
	git-sym show run/$*
	git-sym check run/$*
# Our only integration test, for now.
test:
	python -c 'import pypeflow.pwatcher_workflow; print pypeflow.pwatcher_workflow'
	python -c 'import falcon_kit; print falcon_kit.falcon'
	${MAKE} run-synth0
	${MAKE} -C run/synth0 test

.PHONY: default
