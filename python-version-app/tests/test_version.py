import json
import platform
import subprocess
import sys


def run_version_script(*extra_args):
    """Run version.py as a subprocess and return its CompletedProcess result."""
    result = subprocess.run(
        [sys.executable, "python-version-app/version.py", *extra_args],
        capture_output=True,
        text=True,
    )
    return result


# ---------------------------------------------------------------------------
# Existing tests — no-arg behavior
# ---------------------------------------------------------------------------


def test_output_format():
    """Output should match 'Python X.Y.Z' format."""
    result = run_version_script()
    output = result.stdout.strip()
    assert output.startswith("Python "), f"Expected output to start with 'Python ', got: {output!r}"
    parts = output.split(" ")
    assert len(parts) == 2, f"Expected two space-separated parts, got: {output!r}"
    version_parts = parts[1].split(".")
    assert len(version_parts) == 3, f"Expected major.minor.micro, got: {parts[1]!r}"


def test_output_contains_current_major_minor():
    """Output should contain the current Python major.minor version."""
    expected = f"{sys.version_info.major}.{sys.version_info.minor}"
    result = run_version_script()
    output = result.stdout.strip()
    assert expected in output, (
        f"Expected output to contain '{expected}', got: {output!r}"
    )


def test_exit_code_zero():
    """Script should exit with code 0."""
    result = run_version_script()
    assert result.returncode == 0, f"Expected exit code 0, got: {result.returncode}"


def test_no_stderr_output():
    """Script should not write anything to stderr."""
    result = run_version_script()
    assert result.stderr == "", f"Expected empty stderr, got: {result.stderr!r}"


# ---------------------------------------------------------------------------
# New tests — --version flag
# ---------------------------------------------------------------------------


def test_version_flag_output_format():
    """--version flag should print 'major.minor.micro' with no 'Python' prefix."""
    result = run_version_script("--version")
    output = result.stdout.strip()
    # Must NOT start with "Python"
    assert not output.startswith("Python"), (
        f"--version output should not start with 'Python', got: {output!r}"
    )
    # Must be exactly three numeric parts separated by dots
    parts = output.split(".")
    assert len(parts) == 3, f"Expected major.minor.micro, got: {output!r}"
    for part in parts:
        assert part.isdigit(), f"Each version component must be numeric, got: {part!r}"


def test_version_flag_matches_current_version():
    """--version flag should print the current interpreter's version."""
    v = sys.version_info
    expected = f"{v.major}.{v.minor}.{v.micro}"
    result = run_version_script("--version")
    output = result.stdout.strip()
    assert output == expected, (
        f"Expected --version output '{expected}', got: {output!r}"
    )


def test_version_flag_exit_code_zero():
    """--version flag should exit with code 0."""
    result = run_version_script("--version")
    assert result.returncode == 0, (
        f"Expected exit code 0 for --version, got: {result.returncode}"
    )


def test_version_flag_no_stderr():
    """--version flag should not write anything to stderr."""
    result = run_version_script("--version")
    assert result.stderr == "", (
        f"Expected empty stderr for --version, got: {result.stderr!r}"
    )


# ---------------------------------------------------------------------------
# New tests — --help flag
# ---------------------------------------------------------------------------


def test_help_flag_exit_code_zero():
    """--help flag should exit with code 0."""
    result = run_version_script("--help")
    assert result.returncode == 0, (
        f"Expected exit code 0 for --help, got: {result.returncode}"
    )


def test_help_flag_no_stderr():
    """--help flag output should go to stdout only, with nothing on stderr."""
    result = run_version_script("--help")
    assert result.stderr == "", (
        f"Expected empty stderr for --help, got: {result.stderr!r}"
    )


def test_help_flag_includes_version_flag_description():
    """--help output should mention the --version flag and its description."""
    result = run_version_script("--help")
    output = result.stdout
    assert "--version" in output, (
        f"Expected '--version' in --help output, got: {output!r}"
    )


def test_help_flag_includes_help_flag_description():
    """--help output should mention the -h/--help flag."""
    result = run_version_script("--help")
    output = result.stdout
    assert "--help" in output or "-h" in output, (
        f"Expected '--help' or '-h' in --help output, got: {output!r}"
    )


def test_help_flag_includes_usage_line():
    """--help output should include a usage line."""
    result = run_version_script("--help")
    output = result.stdout.lower()
    assert "usage" in output, (
        f"Expected 'usage' in --help output, got: {result.stdout!r}"
    )


# ---------------------------------------------------------------------------
# New tests — --json flag
# ---------------------------------------------------------------------------


def test_json_flag_exit_code_zero():
    """--json flag should exit with code 0 (not crash)."""
    result = run_version_script("--json")
    assert result.returncode == 0, (
        f"Expected exit code 0 for --json, got: {result.returncode}"
    )


def test_json_flag_no_stderr():
    """--json flag should not write anything to stderr."""
    result = run_version_script("--json")
    assert result.stderr == "", (
        f"Expected empty stderr for --json, got: {result.stderr!r}"
    )


def test_json_flag_output_is_valid_json():
    """--json flag output should be parseable JSON."""
    import json
    result = run_version_script("--json")
    output = result.stdout.strip()
    try:
        json.loads(output)
    except json.JSONDecodeError as e:
        raise AssertionError(f"--json output is not valid JSON: {output!r}") from e


def test_json_flag_output_has_python_version_key():
    """--json output must include a 'python_version' key."""
    import json
    result = run_version_script("--json")
    data = json.loads(result.stdout.strip())
    assert "python_version" in data, (
        f"Expected 'python_version' key in JSON output, got keys: {list(data.keys())}"
    )


def test_json_flag_output_has_os_version_key():
    """--json output must include an 'os_version' key."""
    import json
    result = run_version_script("--json")
    data = json.loads(result.stdout.strip())
    assert "os_version" in data, (
        f"Expected 'os_version' key in JSON output, got keys: {list(data.keys())}"
    )


def test_json_flag_python_version_matches_current():
    """--json python_version should match the running interpreter's version."""
    import json
    v = sys.version_info
    expected = f"{v.major}.{v.minor}.{v.micro}"
    result = run_version_script("--json")
    data = json.loads(result.stdout.strip())
    assert data["python_version"] == expected, (
        f"Expected python_version '{expected}', got: {data['python_version']!r}"
    )


def test_help_flag_includes_json_flag_description():
    """--help output should mention the --json flag."""
    result = run_version_script("--help")
    output = result.stdout
    assert "--json" in output, (
        f"Expected '--json' in --help output, got: {output!r}"
    )


def test_json_flag_output_has_timestamp_key():
    """--json output must include a 'timestamp' key."""
    import json
    result = run_version_script("--json")
    data = json.loads(result.stdout.strip())
    assert "timestamp" in data, (
        f"Expected 'timestamp' key in JSON output, got keys: {list(data.keys())}"
    )


def test_json_flag_timestamp_is_valid_datetime():
    """--json 'timestamp' value must be parseable as an ISO 8601 datetime string."""
    import datetime
    import json
    result = run_version_script("--json")
    data = json.loads(result.stdout.strip())
    try:
        datetime.datetime.fromisoformat(data["timestamp"])
    except (ValueError, KeyError) as e:
        raise AssertionError(
            f"'timestamp' is not a valid ISO 8601 datetime: {data.get('timestamp')!r}"
        ) from e
