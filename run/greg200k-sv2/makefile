falcon:
	fc_run fc_run.cfg
unzip:
	fc_unzip.py fc_unzip.cfg
quiver:
	fc_quiver.py fc_unzip.cfg
clean:
	rm -rf 3-*/ mypwatcher/ pwatcher.dir
cleaner: clean
	rm -rf 0-*/ 1-*/ 2-*/ all.log mypwatcher/ scripts/ sge_log/
symlink:
	python -m falcon_kit.mains.hgap4_adapt --job-output=jo/ --link-dir=.
