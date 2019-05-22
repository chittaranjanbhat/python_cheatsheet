import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
from datetime import datetime
fh = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-4s - %(lineno)04d - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    logger.info('Name: '+name)
    logger.info('Age: '+age)