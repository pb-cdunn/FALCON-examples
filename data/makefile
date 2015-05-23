ECOLI_FASTA:= \
	ecoli.1.subreads.fasta \
	ecoli.2.subreads.fasta \
	ecoli.3.subreads.fasta

ecoli: ${ECOLI_FASTA}
%.fasta:
	${MAKE} -f git-sym.makefile $$(readlink $@)

foo-test:
	${MAKE} -f git-sym.makefile $$(readlink $@)
