import logging


def logging_config():
    """
    Formats taken from:
    https://docs.python.org/3/library/logging.html#logrecord-attributes 
    """
    logging.basicConfig(
        filename="pygarth.log",
        format='%(levelname)s %(asctime)s %(pathname)s:%(lineno)d %(message)s',
        level=logging.INFO
    )