import logging
import sys

FORMAT = '%(asctime)s %(levelname)s - %(threadName)s:%(funcName)s:%(lineno)d  %(message)s'
FORMATTER = logging.Formatter(FORMAT)


def setup_logger(console_level="DEBUG", file_level="DEBUG"):
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    logger.addHandler(setup_file_handler(file_level))
    logger.addHandler(setup_console_handler(console_level))
    return logger


def setup_console_handler(console_level):
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def setup_file_handler(file_level):
    file_handler = logging.FileHandler(filename='log_file.log', mode='w')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(FORMATTER)
    return file_handler


log = setup_logger()
