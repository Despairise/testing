import logging
import logging.handlers


def main_log():
    file_handler = logging.FileHandler('./log/readme.log')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s: %(message)s',
                        handlers=[file_handler])
    logger = logging.getLogger(__name__)
    return logger
