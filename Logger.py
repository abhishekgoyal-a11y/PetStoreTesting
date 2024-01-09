import logging

def init_logger(logger_level='INFO'):
    logger = logging.getLogger()

    if logger_level.upper() == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)
    elif logger_level.upper() == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif logger_level.upper() == 'INFO':
        logger.setLevel(logging.INFO)
    elif logger_level.upper() == 'DEBUG':
        logger.setLevel(logging.DEBUG)
