import logging
import datetime

# logging level; choose from below:
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0
LOG_LEVEL = logging.DEBUG
LOGGER_NAME = "root"
# the file into which to write logs
LOG_FILE = f"./logs/{datetime.datetime.today().strftime('%Y-%m-%d')}.log"
# log message format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"