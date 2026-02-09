PYTHON_VERSION := 3.12
PACKAGE_NAME := $(shell python -c "import configparser; cfg = configparser.ConfigParser(); cfg.read('setup.cfg'); print(cfg['metadata']['name'])")
REPO_ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

# Enable typecheck tools - start with most compatible ones
RUN_MYPY := 1
RUN_PYRIGHT := 1
# Disable tools with significant pandera compatibility issues for now
RUN_TY := 0
RUN_BASEDPYRIGHT := 0
RUN_PYREFLY := 0

export
include shared/Makefile