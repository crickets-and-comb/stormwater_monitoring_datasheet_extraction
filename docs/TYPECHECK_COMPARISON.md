# Type Checker Comparison and Recommendations

## Summary

This repository runs **2 type checkers** successfully: `pytype` and `mypy`. The other tools (`pyright`, `basedpyright`, `ty`, and `pyrefly`) were tested but disabled due to compatibility issues with the project's dependencies, particularly `pandera`.

## Tools Evaluated

### Successfully Enabled

1. **pytype** (Google)
   - **Status**: PASS ✅
   - **Runtime**: ~1s
   - **Configuration**: Uses shared `pytype.cfg`
   - **Notes**: Already present, runs only on Python < 3.13 due to upstream limitations

2. **mypy** (Python Software Foundation)
   - **Status**: PASS ✅
   - **Runtime**: ~2-3s
   - **Configuration**: None (runs with default settings)
   - **Strictness**: Default settings
   - **Community**: Most widely adopted Python type checker, very mature
   - **Notes**: De facto standard for Python type checking, requires `pandas-stubs` for pandas support

### Disabled

3. **pyright** (Microsoft)
   - **Status**: FAIL ❌
   - **Reason**: 67+ errors with pandera's complex type system
   - **Notes**: Would require extensive configuration to work with pandera

4. **basedpyright** (Community fork of pyright)
   - **Status**: FAIL ❌
   - **Reason**: 67+ errors with pandera's complex type system (same as pyright)
   - **Notes**: Drop-in replacement for pyright, but has same pandera compatibility issues

5. **ty** (Astral/Ruff team)
   - **Status**: FAIL ❌
   - **Reason**: Module resolution issues - cannot find `typeguard` and other installed packages
   - **Notes**: Very new tool, still in early development (0.0.x versions). Module resolution needs improvement.

6. **pyrefly** (Meta)
   - **Status**: FAIL ❌
   - **Reason**: 53 errors related to `pandera`'s `CategoricalDtype` usage
   - **Notes**: Cannot handle pandera's advanced typing patterns. Would require significant codebase changes or pandera removal.

## Code Changes Required

Minimal changes were needed to achieve full type checking compliance:

1. **tests/conftest.py**: Changed `config.rootdir` to `config.rootpath` (pytest API change)
2. **src/.../load_datasheets.py**: Added type annotation `dict[str, Any]` to `restructured_json`
3. **src/.../constants.py**: Added `# type: ignore[import-untyped]` for `comb_utils` import (external library)
4. **src/.../schema/schema.py**: Added `# type: ignore[arg-type]` for valid pandas Index comparison (pandas-stubs limitation)
5. **tests/unit/test_schema.py**: Added type parameter to `AbstractContextManager[None]` and `# type: ignore[arg-type]` for test DataFrame
6. **tests/unit/test_load_datasheets.py**: Added type parameters for `AbstractContextManager[None]`, `Callable[..., Any]`, and `dict[str, Any]`

## Runtime Comparison

Total typecheck time (both tools): **~3-4 seconds**

Individual tool performance (approximate):
- pytype: 1s
- mypy: 2-3s

## Strictness Evaluation

1. **mypy** - Configurable, using default settings
2. **pytype** - Google's tool, more lenient with dynamic types

## Maintainer Support & Community

1. **mypy**
   - Maintainer: Python Software Foundation / Jukka Lehtosalo
   - Status: Very mature (10+ years)
   - Community: Largest Python type checker community
   - Support: Excellent documentation, wide adoption

2. **pytype**
   - Maintainer: Google
   - Status: Maintenance mode for Python 3.13+
   - Community: Smaller than mypy
   - Support: Being phased out in favor of other tools

## Recommendations

### Primary Recommendation: **mypy**

**Rationale:**
- Industry standard with the largest community
- Excellent documentation and ecosystem support
- Works well with `pandas` through `pandas-stubs`
- Long-term stability and maintenance guaranteed
- No configuration files needed (runs with defaults)

### Secondary Recommendation: Keep **pytype** for now

**Rationale:**
- Already configured in shared
- Provides additional coverage until Python 3.13+
- Will be phased out later when Python 3.13 support is needed

### Not Recommended

- **pyright/basedpyright**: Incompatible with `pandera`'s complex type system without extensive configuration
- **ty**: Too early in development, module resolution issues
- **pyrefly**: Incompatible with `pandera`'s type system

## Conclusion

This repository successfully runs **2 type checkers** (`pytype` and `mypy`) with minimal code changes and **no configuration files**. The primary recommendation is **mypy** as the industry standard type checker, with `pytype` providing additional coverage until Python 3.13+ support is required.

All typecheck tools pass successfully with **0 errors**.
