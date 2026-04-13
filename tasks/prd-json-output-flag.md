[PRD]
# PRD: JSON Output Flag

## Overview

Add a `--json` flag to the Python version app that outputs environment information in machine-readable JSON format. This helps developers quickly inspect their Python and OS environment in a structured, parseable way — useful for debugging, scripting, and tooling integrations.

## Goals

- Provide a `--json` modifier flag that formats output as a JSON object
- Support combining `--json` with other flags (e.g. `--json --os` returns OS info as JSON)
- When used alone, `--json` outputs both Python version and OS version
- Keep output valid, parseable JSON at all times

## Quality Gates

These commands must pass for every user story:

- `python -m pytest`

## User Stories

### US-001: Add --json flag to CLI argument parser

**Description:** As a developer, I want a `--json` flag recognized by the CLI so that I can request JSON-formatted output.

**Acceptance Criteria:**

- [ ] `--json` is a valid CLI flag (no error when passed)
- [ ] `--help` lists `--json` with a short description
- [ ] Passing `--json` alone does not crash the program

---

### US-002: Output Python version as JSON

**Description:** As a developer, I want `python version_app.py --json` to print the Python version as a JSON object so that I can parse it in scripts.

**Acceptance Criteria:**

- [ ] Running `python version_app.py --json` prints valid JSON to stdout
- [ ] JSON includes a `"python_version"` key with the version string (e.g. `"3.11.4"`)
- [ ] JSON includes an `"os_version"` key with the OS version string
- [ ] Output is valid JSON (parseable by `json.loads`)
- [ ] No extra non-JSON text is printed to stdout

---

### US-003: --json combines with --os flag

**Description:** As a developer, I want `--json --os` to return OS info as JSON so that I can selectively request structured data.

**Acceptance Criteria:**

- [ ] `python version_app.py --json --os` prints valid JSON with `"os_version"` key
- [ ] `python version_app.py --json --os` does NOT include `"python_version"` key (only OS was requested)
- [ ] `python version_app.py --json` (no other flags) includes both `"python_version"` and `"os_version"`

---

### US-004: Write tests for --json flag behavior

**Description:** As a developer, I want automated tests for the `--json` flag so that behavior is verified and regressions are caught.

**Acceptance Criteria:**

- [ ] Test: `--json` alone produces valid JSON with both keys
- [ ] Test: `--json --os` produces JSON with only `"os_version"` key
- [ ] Test: JSON output is parseable via `json.loads`
- [ ] All existing tests continue to pass

## Functional Requirements

- FR-1: The CLI must accept `--json` as an optional flag
- FR-2: When `--json` is passed without other data flags, output must include both `python_version` and `os_version` keys
- FR-3: When `--json` is combined with `--os`, output must include only `os_version`
- FR-4: All JSON output must be valid and parseable
- FR-5: Non-JSON (plain text) output must remain unchanged when `--json` is not passed

## Non-Goals

- CSV or XML output formats
- Writing JSON output to a file (stdout only)
- Pretty-printing / indented JSON (compact single-line is acceptable)
- Adding new data fields beyond Python version and OS version

## Technical Considerations

- Use Python's built-in `json` module for serialization
- Reuse existing flag-parsing logic (argparse) — add `--json` as a `store_true` argument
- Existing `--python` and `--os` flags should remain unchanged in non-JSON mode
- Tests should use `subprocess` or direct function calls to verify output

## Success Metrics

- `python -m pytest` passes with all new tests included
- `python version_app.py --json` outputs valid JSON
- No regressions in existing plain-text output behavior

## Open Questions

- Should `--json` combined with `--python` (if that flag exists) output only `python_version`? Assumed yes, but not explicitly tested in this PRD.
- Should invalid flag combinations (e.g. `--json` with no recognized data flags) return an empty JSON object `{}` or an error?
[/PRD]
