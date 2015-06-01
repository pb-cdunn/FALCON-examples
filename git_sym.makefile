# Cache big-data files.
# This is used by git-sym.
# Note: So-called order-only prerequisites can be useful.
#   http://www.gnu.org/software/make/manual/make.html#Prerequisite-Types
foo:
	cp -f ~/foo $@
m140913_050931_42139_c100713652400000001823152404301535_s1_p0.1.subreads.fasta:
	wget -c https://www.dropbox.com/s/tb78i5i3nrvm6rg/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.1.subreads.fasta
m140913_050931_42139_c100713652400000001823152404301535_s1_p0.2.subreads.fasta:
	wget -c https://www.dropbox.com/s/v6wwpn40gedj470/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.2.subreads.fasta
m140913_050931_42139_c100713652400000001823152404301535_s1_p0.3.subreads.fasta:
	wget -c https://www.dropbox.com/s/j61j2cvdxn4dx4g/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.3.subreads.fasta
lambda-creads.1.fasta:
	cp -f /lustre/hpcprod/cdunn/data/lambda/cx.pb.fasta $@
synth0.fasta:
	cp -f /lustre/hpcprod/cdunn/data/synth0/cx.fasta $@
