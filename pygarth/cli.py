from argparse import ArgumentParser
from pygarth import __version__
import sys
import logging

logger = logging.getLogger(__name__)


def unknown_command_message(unknown_messages: list[str]) -> None:
    logger.info(
        f"The following arguments were ignored: {', '.join(unknown_messages)!r}"
    )


def cli(args=None):
    p = ArgumentParser(
        description="Automatic regression testing harness in Python.",
        conflict_handler="resolve",
    )
    p.add_argument(
        "-v",
        "--version",
        action="version",
        help="Show the version of the program.",
        version=f"PyGARTH {__version__.__version__}",
    )

    p.add_argument(
        "-c",
        "--compare_only",
        help="Only compares the output without executing the tests. The provided option needs to be a directory.",
    )

    p.add_argument(
        "-f",
        "--fast",
        help="Performs minimal file comparison and limited results report.",
    )

    args, unknown = p.parse_known_args(args)
    if unknown:
        unknown_command_message(unknown)

    return args


if __name__ == "__main__":
    cli(sys.argv[1:])
