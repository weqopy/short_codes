import logging
import logging.handlers
import datetime


# 使用 logging 日志模块
# Logger - Handler - Formatter/Filter

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

all_log_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
all_log_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"))

error_log_handler = logging.FileHandler('error.log')
error_log_handler.setLevel(logging.ERROR)
error_log_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(all_log_handler)
logger.addHandler(error_log_handler)

logger.debug('debug msg')
logger.info('info msg')
logger.warning('warning msg')
logger.error('error msg')
logger.critical('critical msg')
