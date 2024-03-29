import datetime
from modules.info_getter import InfoGetter
from modules.info_poster import InfoPoster


class InfoManager:
    def __init__(self) -> None:
        pass

    def forward_daily_sales(self):
        reports = InfoGetter().get_today_sales_reports()

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
                        "SalesDate": datetime.datetime.now().strftime("%Y-%m-%d"),
                        "TransactionCount": str(payments_count),
                        "NetSales": str(net_sales),
                    }
                ]
            }
        }

        InfoPoster().post_daily_report(data)

    def forward_monthly_sales(self):
        reports = InfoGetter().get_month_sales_reports()

        if "net_sales" in reports:
            net_sales = reports["net_sales"]
        else:
            net_sales = 0

        if "payments_count" in reports:
            payments_count = len(reports["payments_count"])
        else:
            payments_count = 0

        data = {
            "SalesDataCollection": {
                "SalesInfo": [
                    {
                        "UnitNo": "TDM-LG-206",
                        "LeaseCode": "t0018733",
                        "SalesDateFrom": "2019-05-01",
                        "SalesDateTo": "2019-05-31",
                        "TransactionCount": str(payments_count),
                        "NetSales": str(net_sales),
                    }
                ]
            }
        }

        InfoPoster().post_monthly_report(data)

    def __get_previous_month(self, current_date: datetime.datetime):
        if current_date.month != 1:
            return current_date.replace(month=current_date.month - 1)
        
        return current_date.replace(month=12).replace(year=current_date.year - 1)