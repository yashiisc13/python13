import logging


def logs():
    logger = logging.getLogger('youtube.Tests.test_run')
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)

    f_handler = logging.FileHandler('report.log')
    formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

    f_handler.setFormatter(formatter)
    logger.addHandler(f_handler)

    return logger
