from loguru import logger
from time import sleep

logger.debug('debug message')

sleep(1)
logger.info('info message')

# logger.add("file_{time}.log")

logger.info(f'info{23} file message')

logger.info("github web editor")
