
from http.client import HTTPException
# from select import select
import requests
import pandas as pd
# from database.db import SessionLocal,Stock
# latest_payload = ""
#     # reqUrl = "https://groww.in/v1/api/stocks_data/v1/tr_live_prices/exchange/NSE/segment/CASH/{}/latest".format(name)
#     # latest_payload_response = requests.request("GET", reqUrl, data=latest_payload,  headers=headersList)
class Stock:
    def __init__(self):
        pass
        # try:
        #     # self._session = SessionLocal()
        # except Exception as e:
        #     raise HTTPException("Can't connect to the DB")

    def get_stocks(self,name,headersList):
        fundamental_payload = ""
        reqUrl = "https://groww.in/v1/api/stocks_data/v1/company/search_id/{}?page=0&size=10".format(name)
        payload_response = requests.request("GET", reqUrl, data=fundamental_payload,  headers=headersList)
        data = payload_response.json()
        return data
        fundamentals = data["header"]
        details = data["details"]
        statistics = data["stats"]
        funds_invested = data["fundsInvested"]
        financialStatement = data["financialStatement"]
        similarAssets = data["similarAssets"]
        
        
        full_name = details["fullName"]
        header = fundamentals["header"]
        user = self._session.query(Stock).first()
        return user
        data_set = pd.json_normalize(fundamentals)
        data_set.to_csv('file1.csv')
        return data
        
async def get_stocks(name,headersList):
    stock = Stock()
    try:
        data = stock.get_stocks(name,headersList)
        return data
    except Exception as e:
            raise HTTPException("Error getting stocks")
