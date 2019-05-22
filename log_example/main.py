import logging
import logging.config
import log_class

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
from datetime import datetime
fh = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-4s - %(lineno)04d - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

if __name__ == '__main__':
    logger.debug('This is a debug message')
    logger.info('This is a info message')
    logger.warning('This is warning message')
    logger.error('This is a error message')
    logger.critical('This is critical message')
    log = log_class.Person('Chittaranjan','27')