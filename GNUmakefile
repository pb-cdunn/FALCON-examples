# Activate virtualenv environment and delegate the rule to makefile.
# We suggest that you not add any rules to 'GNUmakefile'. Instead, customize 'makefile'.
# If you prefer to activate within your shell, then you can simply remove 'GNUmakefile', which
# otherwise always takes precedence.
FALCON_DIR?=../falcon
FALCON_BIN?=${FALCON_DIR}/fc_env/bin

run:
%:
	 . ${FALCON_BIN}/activate; ${MAKE} -f makefile $@
