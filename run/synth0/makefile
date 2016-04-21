# This will show 'shift by 273', but we do not mind if the shift changes,
# since it is circular. We just want output to match input with some shift,
# and maybe with reverse-complement.
go: run
	${MAKE} test
run:
	fc_run1 fc_run.cfg logging.ini
test:
	./check.py
clean:
	\rm -rf 0-*/ 1-*/ 2-*/ *.log mypwatcher/
