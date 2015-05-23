# FALCON-examples
Examples on branches, and a useful place for testing

To run, first build FALCON and its dependencies. In your environment, set FALCON_BIN to your **virtualenv** bin. Then `make run`.

# Branches
The intention is to put different examples on different branches. You can also use this repository as your own workspace. The repo data is lightweight because of **git-sym**.

# git-sym
This is an experimental system which might become a fully supported executable someday. It should be automatic for you.

Its purpose is to separate big-file caching from revision-control. There are several alternatives:

* https://github.com/jedbrown/git-fat
* https://github.com/schacon/git-media
* http://git-annex.branchable.com/
* https://github.com/github/git-lfs

But all those impose the penalty of checksums on the large files. We assert that the large files can be uniquely derived from URLs, versioned in S3 or by filename, etc. We store only symlinks in the git repo.
