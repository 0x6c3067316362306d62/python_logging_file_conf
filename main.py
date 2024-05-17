import logging
import logging.config


if __name__ == '__main__':
    logging.config.fileConfig('config/logging.conf')
    logger = logging.getLogger(__name__)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')



