from pygarth.cli import cli
from pygarth.config_logger import logging_config
import logging

logger = logging.getLogger(__name__)
logging_config()


def main():
    print("Hello PyGARTH! ")
    input_args = cli()


if __name__ == "__main__":
    main()
