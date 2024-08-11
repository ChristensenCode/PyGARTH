from pygarth.cli import cli
from pygarth.config_logger import logging_config
import logging

logger = logging.getLogger(__name__)


def main():
    logging_config()
    cli_arguments = cli()


if __name__ == "__main__":
    main()
