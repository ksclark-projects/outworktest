import subprocess
import sys


def run_version_script():
    """Run version.py as a subprocess and return its stdout output."""
    result = subprocess.run(
        [sys.executable, "python-version-app/version.py"],
        capture_output=True,
        text=True,
    )
    return result


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
