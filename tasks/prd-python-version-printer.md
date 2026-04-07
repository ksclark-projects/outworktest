[PRD]
# PRD: Python Version Printer

## Overview
A simple diagnostic tool for developers to quickly check their current Python version from the command line. The script prints the Python version in a human-readable format and exits cleanly.

## Goals
- Print the current Python version in a simple, human-readable format (e.g. "Python 3.11.4")
- Serve as a lightweight diagnostic utility for local environment troubleshooting

## Quality Gates

These commands must pass for every user story:
- `python -m pytest` — unit test suite

## User Stories

### US-001: Print Current Python Version
**Description:** As a developer, I want to run a script that prints the current Python version so that I can quickly diagnose my local environment.

**Acceptance Criteria:**
- [ ] Running `python python-version-app/version.py` prints the Python version to stdout
- [ ] Output is human-readable (e.g. `Python 3.11.4`)
- [ ] Script exits with code 0 on success
- [ ] `python -m pytest` passes

### US-002: Unit Tests for Version Output
**Description:** As a developer, I want unit tests for the version printer so that I can verify correctness automatically.

**Acceptance Criteria:**
- [ ] A test file exists at `python-version-app/test_version.py`
- [ ] Tests verify the output contains the current major and minor version numbers
- [ ] `python -m pytest python-version-app/test_version.py` passes with no failures

## Functional Requirements
- **FR-1:** The script must print the current Python version to stdout in human-readable format (e.g. `Python 3.11.4`)
- **FR-2:** The script must use the built-in `sys` module — no external dependencies
- **FR-3:** The script must exit with code 0 after successfully printing the version
- **FR-4:** A pytest-compatible test file must cover the version output logic

## Non-Goals
- Version comparison or minimum version enforcement
- JSON or machine-parseable output
- File logging
- CI/CD pipeline integration
- Cross-platform packaging or distribution

## Technical Considerations
- Uses Python built-in `sys` module — no pip installs required
- Main file: `python-version-app/version.py`
- Test file: `python-version-app/test_version.py`
- `sys.version` provides the full version string; `sys.version_info` provides structured access

## Success Metrics
- Script runs without error and prints the Python version on any Python 3.x environment
- `python -m pytest` suite passes with zero failures

## Open Questions
- None
[/PRD]
