PYTHON_VERSION := 3.12
PACKAGE_NAME := $(shell python -c "import configparser; cfg = configparser.ConfigParser(); cfg.read('setup.cfg'); print(cfg['metadata']['name'])")
REPO_ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

# Enable typecheck tools
RUN_MYPY := 1
# Disable tools with pandera compatibility issues
# pyright/basedpyright: many errors with pandera's complex type system
# ty: module resolution issues with typeguard and other imports
# pyrefly: significant pandera CategoricalDtype compatibility issues
RUN_PYRIGHT := 0
RUN_BASEDPYRIGHT := 0
RUN_TY := 0
RUN_PYREFLY := 0

export
include shared/Makefile