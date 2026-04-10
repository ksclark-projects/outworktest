[PRD]
# PRD: OS Version Flag

## Overview
Add a `--os-version` CLI flag and corresponding display to the existing Python version app (`version.py`). When invoked, the flag prints the OS name and version (e.g. `macOS 14.4.1` or `Linux 6.5.0`). Existing no-arg behavior (printing Python version) is preserved.

## Goals
- Add `--os-version` flag that prints the OS name and version to stdout
- Preserve existing behavior: running with no arguments prints Python version only
- Use Python's built-in `platform` module for OS detection
- All existing and new tests pass via `python -m pytest`

## Quality Gates

These commands must pass for every user story:
- `python -m pytest` — Run the full test suite

## User Stories

### US-001: Add --os-version CLI flag
**Description:** As a developer, I want to run `python version.py --os-version` so that I can quickly see the OS name and version of the current machine.

**Acceptance Criteria:**
- [ ] Running `python version.py --os-version` prints the OS name and version (e.g. `macOS 14.4.1` or `Linux 6.5.0`) to stdout
- [ ] The output contains OS name and version only (no architecture or extra text)
- [ ] The script exits with code 0 after printing the OS version
- [ ] Running `python version.py` with no args still prints only the Python version (existing behavior unchanged)
- [ ] The `--help` output lists `--os-version` with a short description

### US-002: Tests for --os-version flag
**Description:** As a developer, I want automated tests for the `--os-version` flag so that regressions are caught automatically.

**Acceptance Criteria:**
- [ ] Test: `--os-version` exits with code 0
- [ ] Test: `--os-version` output is non-empty and contains a string
- [ ] Test: `--os-version` produces no stderr output
- [ ] Test: running with no args still prints Python version (regression guard)
- [ ] All 15+ tests pass via `python -m pytest`

## Functional Requirements
- FR-1: The script must accept `--os-version` as a CLI argument.
- FR-2: When `--os-version` is passed, the script must print the OS name and version (e.g. `macOS 14.4.1`) to stdout and exit with code 0.
- FR-3: OS name and version must be derived using Python's built-in `platform` module (e.g. `platform.system()` and `platform.release()` or `platform.mac_ver()` for macOS).
- FR-4: Running the script with no arguments must preserve existing behavior (print Python version, exit 0).
- FR-5: The `--help` output must include a description for the `--os-version` flag.

## Non-Goals
- No architecture info (e.g. arm64, x86_64) in the output
- No JSON or machine-readable output format
- No importable `get_os_version()` function — CLI flag only
- No combining `--version` and `--os-version` in a single call (each flag works independently)

## Technical Considerations
- Use Python's built-in `platform` module: `platform.system()` for OS name, `platform.release()` for version
- For macOS, consider using `platform.mac_ver()[0]` for a cleaner version string (e.g. `14.4.1` vs kernel version)
- `version.py` already uses `argparse` — add `--os-version` as a new argument to the existing parser

## Success Metrics
- `--os-version` flag outputs a correct OS name and version string on macOS and Linux
- All pytest tests pass (including new OS version tests)
- No regressions in existing `--version` or `--help` behavior

## Open Questions
- None at this time
[/PRD]
