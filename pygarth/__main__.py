from pygarth.cli import cli
from pygarth.config_logger import logging_config
import logging

logger = logging.getLogger(__name__)


def main():
    print("Hello PyGARTH! ")
    input_args = cli.cli()
    x = 1


if __name__ == "__main__":
    main()
