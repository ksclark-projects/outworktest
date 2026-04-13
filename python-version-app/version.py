import argparse
import json
import platform
import sys


def get_version_string():
    """Return the Python version as 'major.minor.micro'."""
    v = sys.version_info
    return f"{v.major}.{v.minor}.{v.micro}"


def get_os_version():
    """Return the OS version string."""
    return platform.version()


def main():
    parser = argparse.ArgumentParser(description="Display the current Python version.")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print the Python version (e.g. 3.12.2) and exit.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output python_version and os_version as a JSON object.",
    )
    args = parser.parse_args()

    if args.json:
        print(json.dumps({
            "python_version": get_version_string(),
            "os_version": get_os_version(),
        }))
    elif args.version:
        print(get_version_string())
    elif args.os_version:
        system = platform.system()
        if system == "Darwin":
            version = platform.mac_ver()[0]
            print(f"macOS {version}")
        else:
            version = platform.release()
            print(f"{system} {version}")
    else:
        print(f"Python {get_version_string()}")

    sys.exit(0)


if __name__ == "__main__":
    main()
