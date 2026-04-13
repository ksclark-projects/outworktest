[PRD]
# PRD: --format Flag for Output Control

## Overview

Add a `--format` flag to the version app CLI that allows developers to control output format (plain or json). This unifies output formatting under a single, explicit flag and deprecates the existing `--json` flag in favor of `--format json`.

## Goals

- Provide a single, explicit `--format` flag for controlling output format
- Support `plain` (default) and `json` output formats
- Deprecate `--json` in favor of `--format json` with a clear warning
- Ensure automated tests cover all format output paths

## Quality Gates

These commands must pass for every user story:

- `python -m pytest` — Automated test suite

## User Stories

### US-001: Add --format flag with plain output

**Description:** As a developer, I want to run the CLI with `--format plain` so that I get the default human-readable output explicitly.

**Acceptance Criteria:**

- [ ] `--format plain` produces the same output as running the CLI with no format flag
- [ ] `--format plain` is the default when `--format` is omitted
- [ ] Invalid format values (e.g. `--format xml`) print a clear error message and exit with a non-zero code
- [ ] Help text (`--help`) documents the `--format` flag and its accepted values

### US-002: Add --format json output

**Description:** As a developer, I want to run the CLI with `--format json` so that I get machine-parseable JSON output.

**Acceptance Criteria:**

- [ ] `--format json` produces valid JSON output
- [ ] JSON output matches the structure previously produced by `--json`
- [ ] `python -m pytest` passes with output assertion tests for `--format json`

### US-003: Deprecate --json flag

**Description:** As a developer using the old `--json` flag, I want to see a deprecation warning so that I know to migrate to `--format json`.

**Acceptance Criteria:**

- [ ] Running `--json` still produces JSON output (no breaking change)
- [ ] A deprecation warning is printed to stderr: `Warning: --json is deprecated. Use --format json instead.`
- [ ] `python -m pytest` includes a test asserting the warning is emitted when `--json` is used

## Functional Requirements

- FR-1: The CLI must accept a `--format` argument with allowed values: `plain`, `json`
- FR-2: When `--format` is omitted, output defaults to `plain`
- FR-3: When `--format json` is passed, output must be valid, parseable JSON
- FR-4: When `--format plain` is passed, output must be identical to the current default output
- FR-5: When an unsupported format value is passed, the CLI must print an error to stderr and exit with code 1
- FR-6: The existing `--json` flag must remain functional but emit a deprecation warning to stderr
- FR-7: The `--help` output must document `--format` and list accepted values

## Non-Goals

- `--format table` or `--format csv` support (future enhancement)
- Making `--format` combinable with other flags like `--os` or `--python` (out of scope for this iteration)
- Removing the `--json` flag entirely (deprecation only, no removal)
- Any GUI or interactive output modes

## Technical Considerations

- Deprecation warning for `--json` should go to stderr to avoid breaking pipe-based consumers
- Existing `--json` tests should be updated to account for the new warning on stderr
- Consider using `argparse` choices to restrict `--format` values and auto-generate help text

## Success Metrics

- `--format json` output is byte-for-byte equivalent to previous `--json` output
- All existing tests pass after the change
- New tests cover: plain format, json format, invalid format, and `--json` deprecation warning

## Open Questions

- Should the deprecation warning for `--json` also be surfaced in `--help` output?
- Is there a target version or timeline for fully removing `--json`?
[/PRD]
