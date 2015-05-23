# Cache big-data files and create symlinks.
# To use, create a symlink into ${GIT_SYM_DIR}, and then simply build it.
# Be sure to 'make setup-cache' once first, or add so-called order-only prerequisites.
#   http://www.gnu.org/software/make/manual/make.html#Prerequisite-Types
#
# This can become a real program someday. For now, keep it simple by recording exact build rules here.
GIT_SYM_DIR:=../.git/git-sym
GIT_SYM_CACHE:=${HOME}/git-sym-cache

${GIT_SYM_DIR}/%: ${GIT_SYM_CACHE}/% | ${GIT_SYM_DIR}
	ln -sf $< $@

${GIT_SYM_CACHE}/foo: | ${GIT_SYM_CACHE}
	cp -f ~/foo $@
${GIT_SYM_CACHE}/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.1.subreads.fasta: | ${GIT_SYM_CACHE}
	cd $(dirname $@); wget -c https://www.dropbox.com/s/tb78i5i3nrvm6rg/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.1.subreads.fasta
${GIT_SYM_CACHE}/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.2.subreads.fasta: | ${GIT_SYM_CACHE}
	cd $(dirname $@); wget -c https://www.dropbox.com/s/v6wwpn40gedj470/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.2.subreads.fasta
${GIT_SYM_CACHE}/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.3.subreads.fasta: | ${GIT_SYM_CACHE}
	cd $(dirname $@); wget -c https://www.dropbox.com/s/j61j2cvdxn4dx4g/m140913_050931_42139_c100713652400000001823152404301535_s1_p0.3.subreads.fasta

setup-cache: | ${GIT_SYM_CACHE}

${GIT_SYM_DIR} ${GIT_SYM_CACHE}:
	mkdir -p $@
