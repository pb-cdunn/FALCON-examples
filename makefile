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
	python -c 'import pypeflow.common; print pypeflow.common'
	python -c 'import falcon_kit; print falcon_kit.falcon'
	${MAKE} run-synth0
	${MAKE} -C run/synth0 test
	#${MAKE} -C run/synth0 clean
	#${MAKE} -C run/synth0 go0 # still test the old pypeflow too, for now
	${MAKE} -C run/synth0 clean
	${MAKE} -C run/synth0 go1 # should be the same as go

.PHONY: default
