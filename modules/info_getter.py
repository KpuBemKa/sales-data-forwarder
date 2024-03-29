import json
import requests
import logging
import datetime

from api_keys import GET_KEY, GET_SECRET
from settings import LOGGER_NAME


logger = logging.getLogger(LOGGER_NAME)


DAY_FORMAT_STR = "%Y-%m-%d+00:00"

CLIENT_ID = "tucano"

REQUEST_HEADER = {
    "API-AUTHENTICATION": f"{GET_KEY}:{GET_SECRET}",
    "content-type": "application/json",
}


class InfoGetter:
    def __init__(self) -> None:
        pass

    def get_month_sales_reports(self) -> dict:
        range_to = datetime.datetime.now().replace(day=1)
        range_from = self.__get_previous_month(range_to)

        req_result = requests.get(
            url=self.__make_sales_reports_get_url(
                f"{range_from.strftime(DAY_FORMAT_STR)}", f"{range_to.strftime(DAY_FORMAT_STR)}"
            ),
            headers=REQUEST_HEADER,
        )

        logger.debug(req_result.text)

        return json.loads(req_result.json())

    def get_today_sales_reports(self) -> dict:
        range_to = datetime.datetime.now()
        range_from = range_to - datetime.timedelta(days=1)

        req_result = requests.get(
            url=self.__make_sales_reports_get_url(
                f"{range_from.strftime(DAY_FORMAT_STR)}", f"{range_to.strftime(DAY_FORMAT_STR)}"
            ),
            headers=REQUEST_HEADER,
        )

        logger.debug(req_result.text)

        return req_result.json()[0]
    
    def __get_previous_month(self, current_date: datetime.datetime):
        if current_date.month != 1:
            return current_date.replace(month=current_date.month - 1)
        
        return current_date.replace(month=12).replace(year=current_date.year - 1)

    def __make_sales_reports_get_url(self, range_from: str, range_to: str) -> str:
        return (
            f"https://{CLIENT_ID}.revelup.com/reports/sales_summary/json/"
            "?posstation=&employee=&show_unpaid=1&show_irregular=1"
            f"&range_from={range_from}&range_to={range_to}&establishment=1&format=json"
        )
