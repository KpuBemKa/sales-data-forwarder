import datetime
from modules.info_getter import InfoGetter
from modules.info_poster import InfoPoster


DATE_FORMAT_STR = "%Y-%m-%d"


class InfoManager:
    def __init__(self) -> None:
        pass

    def forward_daily_sales(self) -> int:
        (result_code, reports) = InfoGetter().get_today_sales_reports()

        if result_code != 200:
            return result_code

        if "net_sales" in reports:
            net_sales = reports["net_sales"]
        else:
            net_sales = 0

        if "payments" in reports:
            payments_count = len(reports["payments"])
        else:
            payments_count = 0

        data = {
            "SalesDataCollection": {
                "SalesInfo": [
                    {
                        "UnitNo": "TDM-LG-206",
                        "LeaseCode": "t0018733",
                        "SalesDate": datetime.datetime.now().strftime(DATE_FORMAT_STR),
                        "TransactionCount": str(payments_count),
                        "NetSales": str(net_sales),
                    }
                ]
            }
        }

        return InfoPoster().post_daily_report(data)

    def forward_monthly_sales(self):
        (result_code, reports) = InfoGetter().get_month_sales_reports()

        if result_code != 200:
            return result_code

        if "net_sales" in reports:
            net_sales = reports["net_sales"]
        else:
            net_sales = 0

        if "payments" in reports:
            payments_count = len(reports["payments"])
        else:
            payments_count = 0

        date_to = datetime.datetime.now().replace(day=1)

        data = {
            "SalesDataCollection": {
                "SalesInfo": [
                    {
                        "UnitNo": "TDM-LG-206",
                        "LeaseCode": "t0018733",
                        "SalesDateFrom": self.__get_previous_month(date_to).strftime(
                            DATE_FORMAT_STR
                        ),
                        "SalesDateTo": date_to.strftime(DATE_FORMAT_STR),
                        "TransactionCount": str(payments_count),
                        "NetSales": str(net_sales),
                    }
                ]
            }
        }

        return InfoPoster().post_monthly_report(data)

    def __get_previous_month(self, current_date: datetime.datetime):
        if current_date.month != 1:
            return current_date.replace(month=current_date.month - 1)

        return current_date.replace(month=12).replace(year=current_date.year - 1)
