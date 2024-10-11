from argparse import ArgumentParser
from pygarth import __version__


def cli(args=None):
    p = ArgumentParser(
        description="Automatic regression testing harness written in Python.",
        conflict_handler="resolve",
    )
    p.add_argument(
        "-v",
        "--version",
        action="version",
        help="Gives the version of pygarth.",
        version=f"PyGARTH {__version__}",
    )
    p.add_argument(
        "-td",
        "--test_directory",
        help="Location of test suite to be executed.",
    )
    p.add_argument(
        "-p",
        "--pattern",
        help="Finds tests that follow the provided pattern using glob formatting.",
    )

    args, unknown = p.parse_known_args(args)
    print("Hello from CLI!")

    return args


if __name__ == "__main__":
    import sys

    cli(sys.argv[1:])
