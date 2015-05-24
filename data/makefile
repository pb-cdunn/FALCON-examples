ECOLI_FASTA:= \
	ecoli.1.subreads.fasta \
	ecoli.2.subreads.fasta \
	ecoli.3.subreads.fasta

ecoli: ${ECOLI_FASTA}
ecoli2: ecoli
%.fasta:
	${MAKE} -f git-sym.makefile $$(readlink $@)

foo-test:
	${MAKE} -f git-sym.makefile $$(readlink $@)
