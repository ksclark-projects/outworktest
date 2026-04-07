import argparse
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
    args = parser.parse_args()

    if args.version:
        print(get_version_string())
    else:
        print(f"Python {get_version_string()}")

    sys.exit(0)


if __name__ == "__main__":
    main()
