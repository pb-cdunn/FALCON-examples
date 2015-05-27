ECOLI_FASTA:= \
	ecoli.1.subreads.fasta \
	ecoli.2.subreads.fasta \
	ecoli.3.subreads.fasta

ecoli: ${ECOLI_FASTA}
ecoli2: ecoli
lambda: lambda-creads.fasta lambda-hgap-3.creads.fasta
lambda-hgap: lambda-hgap-3.creads.fasta
%.fasta:
	git-sym update $@

foo-test:
	git-sym update $@
