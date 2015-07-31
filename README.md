# FALCON-examples
Examples, with test-cases, and a useful place for testing

To run, first build FALCON and its dependencies, and set-up your environment. (See FALCON-integrate in GitHub.) Then:
```
make run-ecoli
```
We do not recommend piping the output, since if you need to stop early (with Ctrl-C aka KeyboardInterrupt), your program might be killed before it has time to `qdel` the outstanding jobs.

## Environment
One way to set-up your environment is to use Python **virtualenv**. Before running these examples, activate your virtualenv in your shell or via FALCON-integrate.

# Data
## `*.fofn`
These are "files of filenames". Since they are in the repo, they should be relative paths. (Relative to the current directory when they are used. But that is wrong. It should be relative to their own location. TODO)

## Files
The repo source is lightweight because it contains symlinks instead of the contents of large files. These are managed by **git-sym**.

## [git-sym](https://github.com/cdunn2001/git-sym)
This separates big-file caching from revision-control. There are several alternatives:

# `data` directories
Relying on **git-sym**, symlinks to the data are stored in `data/` sub-directories. The files should point (relatively) into `.git_sym/`, which contains more symlinks to a cache directory. `git_sym.makefile` should include a rule to produce files for those symlinks.
