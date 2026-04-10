import argparse
import json
import platform
import sys


def get_version_string():
    """Return the Python version as 'major.minor.micro'."""
    v = sys.version_info
    return f"{v.major}.{v.minor}.{v.micro}"


def main():
    parser = argparse.ArgumentParser(description="Display the current Python version.")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print the Python version (e.g. 3.12.2) and exit.",
    )
    parser.add_argument(
        "--os-version",
        action="store_true",
        help="Print the OS name and version (e.g. macOS 14.4.1) and exit.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output python_version and os_version as a JSON object and exit.",
    )
    parser.add_argument(
        "--os",
        action="store_true",
        help="When combined with --json, restrict output to only os_version.",
    )
    args = parser.parse_args()

    if args.json:
        system = platform.system()
        if system == "Darwin":
            os_ver = f"macOS {platform.mac_ver()[0]}"
        else:
            os_ver = f"{system} {platform.release()}"
        if args.os:
            print(json.dumps({"os_version": os_ver}))
        else:
            print(json.dumps({"python_version": get_version_string(), "os_version": os_ver}))
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
