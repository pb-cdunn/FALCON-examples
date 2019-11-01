falcon:
	fc_run fc_run.cfg
unzip:
	fc_unzip.py fc_unzip.cfg
quiver:
	fc_quiver.py fc_unzip.cfg
clean:
	rm -rf 3-unzip/* 4-quiver/* mypwatcher/ pwatcher.dir
cleaner: clean
	rm -rf 0-rawreads/* 1-preads_ovl/* 2-asm-falcon/* all.log mypwatcher/ scripts/ sge_log/
symlink:
	python3 -m falcon_kit.mains.hgap4_adapt --job-output=jo/ --link-dir=.
