# FALCON-examples
Examples, with test-cases, and a useful place for testing

To run, first build FALCON and its dependencies. In your environment, set FALCON_BIN to your **virtualenv** bin. Then `make run-EXAMPLE`.
```
export FALCON_BIN=`pwd`/../FALCON/fc_env/bin
make run-ecoli
```
We do not recommend piping the output, since if you need to stop early (with Ctrl-C aka KeyboardInterrupt), your program might be killed before it has time to `qdel` the outstanding jobs.

# `*.fofn`
These are "files of filenames". Since they are in the repo, they should be relative paths. WORKING ON THIS...

# `data` directory
The repo data is lightweight because it contains symlink instead of the contents of large files.

Symlinks to the data are stored in `data/`. These should point into `../.git/git-sym/`, which contains more symlink to a cache directory, and `data/git-sym/makefile` should include a rule to produce files for those symlinks.

# git-sym

This is an experimental system which might become a fully supported executable someday. It should be automatic for you.

Its purpose is to separate big-file caching from revision-control. There are several alternatives:

* https://github.com/jedbrown/git-fat
* https://github.com/schacon/git-media
* http://git-annex.branchable.com/
* https://github.com/github/git-lfs

But all those impose the penalty of checksums on the large files. We assert that the large files can be uniquely derived from URLs, versioned in S3 or by filename, etc. We store only symlinks in the git repo.
