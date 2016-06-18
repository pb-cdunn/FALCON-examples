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
m140913_050931_42139_c100713652400000001823152404301535_s1_p0.1.subreads.fasta:
	wget -c https://www.dropbox.com/s/tb78i5i3nrvm6rg/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.1.subreads.fasta
m140913_050931_42139_c100713652400000001823152404301535_s1_p0.2.subreads.fasta:
	wget -c https://www.dropbox.com/s/v6wwpn40gedj470/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.2.subreads.fasta
m140913_050931_42139_c100713652400000001823152404301535_s1_p0.3.subreads.fasta:
	wget -c https://www.dropbox.com/s/j61j2cvdxn4dx4g/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.3.subreads.fasta
lambda-creads.1.fasta:
	cp -f /lustre/hpcprod/cdunn/data/lambda/cx.pb.fasta $@
lambda-hgap-3.creads.fasta:
	cp -f /lustre/hpcprod/cdunn/data/lambda/hgap-3.corrected.fasta $@
synth0.pb.fasta:
	wget -O - https://www.dropbox.com/s/a80t8ll29gvt883/cx.pb.fasta.gz | zcat > $@
	#cp -f /lustre/hpcprod/cdunn/data/synth0/cx.pb.fasta $@
synth0-circ-20.pb.fasta:
	wget -O - https://www.dropbox.com/s/bjhcvp05u46o2qy/circ-20.pb.fasta.gz | zcat > $@
	#cp -f /lustre/hpcprod/cdunn/data/synth0/circ-20.pb.fasta $@
synth0.ref.fasta:
	wget -O - https://www.dropbox.com/s/jz0m0n2a1b19xyd/from.fasta.gz | zcat > $@
	#cp -f /lustre/hpcprod/cdunn/data/synth0/from.fasta $@
arab-creads.fasta:
	cp -f /lustre/hpcprod/cdunn/data/arab_test/corrected.fasta $@
