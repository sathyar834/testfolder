import logging.config
import logging

logging.config.fileConfig('F:/Shyam Automation/script folder scrap/logtestfolder/config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def get_logger():
  logger.info('hello')

get_logger()