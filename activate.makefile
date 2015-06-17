# (This used to be GNUmakefile, but it is not necessary anymore. Activate your virtualenv in your shell or via FALCON-integrate.)
# Activate virtualenv environment and delegate the rule to makefile.
# We suggest that you not add any rules to 'GNUmakefile'. Instead, customize 'makefile'.
# If you prefer to activate within your shell, then you can simply remove 'GNUmakefile', which
# otherwise always takes precedence.
FALCON_DIR?=../FALCON
FALCON_BIN?=${FALCON_DIR}/fc_env/bin

run:
%:
	 . ${FALCON_BIN}/activate; ${MAKE} -f makefile $@
