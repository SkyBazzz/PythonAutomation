import importlib
import argparse
import logging

FORMAT = '%(asctime)s %(levelname)s - %(threadName)s:%(funcName)s:%(lineno)d  %(message)s'


def get_package_path(package_name, file_level, console_level):
    logger = setup_file_handler(file_level)
    logger.addHandler(setup_console_handler(console_level))
    try:
        module = importlib.import_module(package_name)
        logger.warning(module.__doc__)
        logger.info(f'Path: {module.__file__}')
        logger.debug(f'Version: {module.__version__}')
    except AttributeError as ae:
        logger.error(ae)
    except ModuleNotFoundError as e:
        logger.error(repr(e))


def setup_file_handler(file_level):
    logging.basicConfig(filename='log_file.log', filemode='w', level=file_level, format=FORMAT)
    logger = logging.getLogger(__name__)
    return logger


def setup_console_handler(console_lvl):
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(FORMAT)
    console_handler.setLevel(console_lvl)
    console_handler.setFormatter(formatter)

    return console_handler


def parse_cmd_args():
    package_help = 'Package name'
    console_level_log_help = "Logging level for console"
    file_level_log_help = "Logging level for file"

    parser = argparse.ArgumentParser()
    parser.add_argument('pack', help=package_help)
    parser.add_argument('-file-level', '--fl', nargs='?', default='INFO', help=file_level_log_help)
    parser.add_argument('-console-level', '--cl', nargs='?', default='INFO', help=console_level_log_help)

    cmd = parser.parse_args()

    return cmd.pack, cmd.fl, cmd.cl


if __name__ == '__main__':
    get_package_path(*parse_cmd_args())
