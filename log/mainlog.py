import logging
import logging.handlers


def main_log(logger):
    logger.setLevel(logging.WARNING)
    fh = logging.handlers.RotatingFileHandler(filename='log/readme.log', backupCount=50)
    fh.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(message)s :: %(levelname)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
