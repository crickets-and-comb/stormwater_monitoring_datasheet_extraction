# Type Checker Comparison and Recommendations

## Summary

This repository now runs **4 type checkers** successfully: `pytype`, `pyright`, `mypy`, and `basedpyright`. Two tools (`ty` and `pyrefly`) were tested but disabled due to compatibility issues with the project's dependencies, particularly `pandera`.

## Tools Evaluated

### Successfully Enabled

1. **pytype** (Google)
   - **Status**: PASS ✅
   - **Runtime**: ~1s
   - **Configuration**: Uses shared `pytype.cfg`
   - **Notes**: Already present, runs only on Python < 3.13 due to upstream limitations

2. **pyright** (Microsoft)
   - **Status**: PASS ✅
   - **Runtime**: ~1-2s
   - **Configuration**: `pyrightconfig.json` (basic mode)
   - **Strictness**: Configurable, running in "basic" mode
   - **Community**: Very active, official VS Code extension, maintained by Microsoft
   - **Notes**: Industry standard, excellent performance

3. **mypy** (Python Software Foundation)
   - **Status**: PASS ✅
   - **Runtime**: ~2-3s
   - **Configuration**: `mypy.ini`
   - **Strictness**: Configurable, currently set to balanced strictness
   - **Community**: Most widely adopted Python type checker, very mature
   - **Notes**: De facto standard for Python type checking, requires `pandas-stubs` for pandas support

4. **basedpyright** (Community fork of pyright)
   - **Status**: PASS ✅
   - **Runtime**: ~1-2s
   - **Configuration**: Uses same `pyrightconfig.json` as pyright
   - **Strictness**: Generally stricter than pyright by default
   - **Community**: Active community fork with enhanced features
   - **Notes**: Drop-in replacement for pyright with additional checks

### Disabled

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
3. **src/.../schema/schema.py**: Added `# type: ignore[arg-type]` for valid pandas Index comparison
4. **tests/unit/test_schema.py**: Added `# type: ignore[arg-type]` for test DataFrame type conversion

## Runtime Comparison

Total typecheck time (all 4 tools): **~7-8 seconds**

Individual tool performance (approximate):
- pytype: 1s
- pyright: 1-2s
- mypy: 2-3s
- basedpyright: 1-2s

## Strictness Evaluation

From most to least strict:
1. **basedpyright** - Enhanced version of pyright with additional checks
2. **mypy** - Highly configurable, currently in balanced mode
3. **pyright** - Microsoft's tool, running in "basic" mode
4. **pytype** - Google's tool, more lenient with dynamic types

## Maintainer Support & Community

1. **mypy**
   - Maintainer: Python Software Foundation / Jukka Lehtosalo
   - Status: Very mature (10+ years)
   - Community: Largest Python type checker community
   - Support: Excellent documentation, wide adoption

2. **pyright**
   - Maintainer: Microsoft
   - Status: Active development
   - Community: Large, integrated with VS Code
   - Support: Professional support through Microsoft

3. **basedpyright**
   - Maintainer: Community (DetachHead)
   - Status: Active fork
   - Community: Growing, enthusiastic contributors
   - Support: Community-driven

4. **pytype**
   - Maintainer: Google
   - Status: Maintenance mode for Python 3.13+
   - Community: Smaller than mypy/pyright
   - Support: Being phased out in favor of other tools

## Recommendations

### Primary Recommendation: **mypy**

**Rationale:**
- Industry standard with the largest community
- Excellent documentation and ecosystem support
- Highly configurable for different strictness levels
- Works well with `pandas` through `pandas-stubs`
- Long-term stability and maintenance guaranteed

### Secondary Recommendation: **pyright** or **basedpyright**

**Rationale:**
- Faster than mypy
- Better VS Code integration
- `basedpyright` offers stricter checking if desired
- Good for catching different classes of errors

### Recommended Configuration

**Option 1: Maximum Coverage (Current Setup)**
- Enable: `mypy`, `pyright`, `basedpyright`, `pytype`
- Runtime: ~7-8 seconds
- Benefit: Maximum error detection across different checker philosophies

**Option 2: Balanced**
- Enable: `mypy`, `basedpyright`
- Runtime: ~4-5 seconds
- Benefit: Good coverage with faster execution

**Option 3: Minimal (If speed is critical)**
- Enable: `mypy` only
- Runtime: ~2-3 seconds
- Benefit: Industry standard with fastest single-tool checking

### Do Not Recommend

- **pytype**: Being phased out by Google, doesn't support Python 3.13+
- **ty**: Too early in development, module resolution issues
- **pyrefly**: Incompatible with `pandera`'s type system

## Conclusion

This repository successfully runs **4 type checkers** with minimal code changes and appropriate configurations. The recommended setup is to keep **mypy** as the primary checker, with **basedpyright** as a secondary strict checker. This provides excellent type safety while maintaining reasonable build times.

All typecheck tools pass successfully with **0 errors**.
