# Contributing to stormwater_monitoring_datasheet_extraction

Thank you for your interest in contributing to stormwater_monitoring_datasheet_extraction! We welcome your ideas for improving this package, documentation, or any other aspect of the project.

## Getting Started

Before opening a pull request (PR), please follow these procedures and guidelines:

1. **Read our [Code of Conduct](./CODE_OF_CONDUCT.md)** to keep our community approachable and respectable.

2. **Open an issue first.** Only open a PR after receiving explicit approval from an admin in response to an issue. This helps us:
   - Avoid unnecessary workflow runs (which cost money).
   - Refine your request together.
   - Check if we're already working on a solution.
   - Ensure your contribution aligns with project goals.

3. **Keep focused scope.** Each issue/PR should be limited to a specific, well-defined change. This is especially important for PRs. We prefer relatively small, focused contributions over sprawling changes.

## Bug Reports

When reporting bugs, please include:

- **Minimal reproducible example** - The smallest code sample that reproduces the issue.
- **Environment details** - OS, Python version, package versions, etc.
- **Full stack trace** - Complete error output and failing call.

## Pull Request Guidelines

### Code Quality Standards

#### Testing Requirements
- **Add test coverage for every piece of expected behavior**
  - Bug fixes: Create a test that reproduces the bug and proves it's fixed.
  - New features: Create tests that prove the feature works as intended.
  - Deprecations: Create a test that proves the feature is deprecated.

#### Function Design
- **Single responsibility**: Functions should do one discrete thing or wrap a set of discrete calls.
- **Size limit**: Keep functions under 50 lines when possible.
- **Single exit point**: Functions should have only one return statement.
- **No externalities**: Functions should only modify objects within their own scope.

#### Type Safety
- Python:
  - **Static typing**: Use type hints in function/method signatures and returns.
  - **Variable typing**: Use type hints in variable/member declarations where helpful.
  - **Constants**: Use `typing.Final` to typehint constants and treat them as immutable.
  - **Runtime checking**: Use runtime typechecking like:
    - `typeguard.typechecked` decorator
    - `pandera.schema`
    - `pandera.check_types` decorator
    - etc.

#### Code Documentation
- **Self-documenting code**:
  - Use meaningful naming conventions.
  - Use docstrings for functions, classes, methods, and modules.
  - Comments should provide context, not explain what the code does.
  - Keep comments few and purposeful.
- **Docstring format**: Follow the [Google Python style guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
- **Prose quality**: Copy edit all prose (spelling, grammar, fact check, link check) including comments, error messages, and documentation. Write like you're writing to a human.

#### TODO Management
- **Avoid TODOs**: Limit the TODOs you leave in code.
- **Tag remaining TODOs**: All TODOs should be linked to open issues.
- **Clean up**: Remove TODOs when implementing features or fixes.

## Development Workflow

### Before Submitting
1. Ensure all QC and tests pass locally by running `make full`.
2. Update documentation as needed.
3. Try features and review documentation in a "live" test where possible. E.g., open the documentation in your browser and inspect your updates, or stage the app in a test environment and manually try your new feature.

### Code Review Process
- All changes require review before merging.
- Address feedback promptly and respectfully.
- Be open to suggestions and improvements.
- Maintain constructive dialogue throughout the review process.

## Questions or Need Help?

If you have questions about contributing or need help getting started:

1. Check the existing documentation.
2. Open an issue to discuss your contribution.
3. Reach out to the maintainers through appropriate channels.

We appreciate your contributions and look forward to working with you!
