# Cache big-data files.
# This is used by git-sym.
# Paths here should be absolute, but targets should be just filenames, sans path.
# Note: '/lustre' paths are PacBio-internal.
# Note: So-called order-only prerequisites can be useful.
#   http://www.gnu.org/software/make/manual/make.html#Prerequisite-Types
foo:
	# This is just for testing git-sym. Sorry for touching home dir.
	-touch ~/foo
	cp -f ~/foo $@
lambda-creads.1.fasta:
	cp -f /lustre/hpcprod/cdunn/data/lambda/cx.pb.fasta $@
lambda-hgap-3.creads.fasta:
	cp -f /lustre/hpcprod/cdunn/data/lambda/hgap-3.corrected.fasta $@
synth0.pb.fasta:
	curl -L https://www.dropbox.com/s/a80t8ll29gvt883/cx.pb.fasta.gz | zcat > $@
	#cp -f /lustre/hpcprod/cdunn/data/synth0/cx.pb.fasta $@
synth0-circ-20.pb.fasta:
	curl -L https://www.dropbox.com/s/bjhcvp05u46o2qy/circ-20.pb.fasta.gz | zcat > $@
	#cp -f /lustre/hpcprod/cdunn/data/synth0/circ-20.pb.fasta $@
synth0.ref.fasta:
	curl -L https://www.dropbox.com/s/jz0m0n2a1b19xyd/from.fasta.gz | zcat > $@
	#cp -f /lustre/hpcprod/cdunn/data/synth0/from.fasta $@
arab-creads.fasta:
	cp -f /lustre/hpcprod/cdunn/data/arab_test/corrected.fasta $@
synth5k.2016-11-02:
	curl -kL https://downloads.pacbcloud.com/public/data/git-sym/synth5k.2016-11-02.tgz | tar xvfz -
ecoli.m140913_050931_42139_c100713652400000001823152404301535_s1_p0:
	curl -L https://downloads.pacbcloud.com/public/data/git-sym/ecoli.m140913_050931_42139_c100713652400000001823152404301535_s1_p0.subreads.tar | tar xvf -
greg200k-sv2.2:
	curl -L https://downloads.pacbcloud.com/public/data/git-sym/greg200k-sv2.2.tar | tar xvf -
