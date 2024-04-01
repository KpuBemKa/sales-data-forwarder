import logging
import sys

from modules.info_manager import InfoManager

from modules.log import setup_custom_logger
from settings import LOGGER_NAME


setup_custom_logger(LOGGER_NAME)
logger = logging.getLogger(LOGGER_NAME)


def main():
    if len(sys.argv) < 2:
        InfoManager().forward_monthly_sales()
        return

    # argument #1 is next after file name
    run_code = sys.argv[1]

    match str(run_code):
        case "0":
            result = InfoManager().forward_daily_sales()

        case "1":
            result = InfoManager().forward_monthly_sales()

        case "-help":
            print("0 - forward daily sales;\n1 - forward monthly sales;")

        case _:
            logger.error("Unrecognized run code. Exiting...")
            result = -1

    if result != 200:
        logger.error(f"FORWARDING ERROR: {result}")


if __name__ == "__main__":
    main()
