import logging

from modules.info_manager import InfoManager

from modules.log import setup_custom_logger
from settings import LOGGER_NAME


setup_custom_logger(LOGGER_NAME)
logger = logging.getLogger(LOGGER_NAME)


def main():
    InfoManager().forward_daily_sales()


if __name__ == "__main__":
    main()
