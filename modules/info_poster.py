import requests
import logging

from settings import LOGGER_NAME
from api_keys import POST_KEY


logger = logging.getLogger(LOGGER_NAME)


MONTHLY_SALES_URL = "https://apidev.emaar.com/etenantsales/casualsales"
DAILY_SALES_URL = "https://apidev.emaar.com/etenantsales/dailysales"

REQUEST_HEADER = {
    "x-apikey": f"{POST_KEY}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}


class InfoPoster:
    def __init__(self) -> None:
        pass

    def post_monthly_report(self, data: dict) -> int:
        return self.__post_report(MONTHLY_SALES_URL, data)

    def post_daily_report(self, data: dict) -> int:
        return self.__post_report(DAILY_SALES_URL, data)

    def __post_report(self, url: str, data: dict) -> int:
        logger.debug(f"Sending POST request to `{url}` with ...\n{data}")
        req_result = requests.post(url=url, headers=REQUEST_HEADER, json=data)

        status_code = req_result.status_code

        if status_code != 200:
            logger.error(f"POST error:\n{req_result.text}")

        return status_code
