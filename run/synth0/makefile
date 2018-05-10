# This will show 'shift by 273', but we do not mind if the shift changes,
# since it is circular. We just want output to match input with some shift,
# and maybe with reverse-complement.
FC_CFG?=fc_run.cfg

go: run
	${MAKE} test
run:
	fc_run ${FC_CFG} logging.json
test:
	./check.py
clean:
	\rm -f *.log mypwatcher/
	\rm -rf 0-rawreads/* 1-preads_ovl/* 2-asm-falcon/*
