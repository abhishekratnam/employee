import imp
from optparse import Option
from pickletools import float8, long4
from tokenize import Double
from turtle import update
from fastapi import FastAPI, Path
from typing import Optional
from models.stockModels import Stocks
import requests
import pandas as pd
from controller import stock_controller
# from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
stock = FastAPI()



@stock.get("/get-by-name")
async def get_Stocks(*, name: Optional[str] = None):
    if name is None:
        return {"Message":"Please enter the name"}
    
    headersList = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/538.69 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/538.38",
        "Accept": "application/json",
        "Accept": "text/plain",
        "Content-Encoding": "br",
        "Connection": "close",
        "Content-Encoding": "gzip",
        "Content-Encoding": "deflate",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJjcmVhdGVkQXRcIjpcIjIwMjItMDctMjBUMTI6Mjg6NTQuMTk2KzAwOjAwXCIsXCJ1c2VyQWNjb3VudElkXCI6XCJBQ0M5NzQ2MDUwNTY5MjcyXCIsXCJpc1N1Y2Nlc3NcIjp0cnVlLFwic2Vzc2lvbklkXCI6XCIwYTZlZGMzYy1jMDllLTRmNTYtYTlmZi0yM2JkM2QyNmM0ZGNcIixcImlwQWRkcmVzc1wiOlwiMTIyLjE2Mi4xNDYuMjUsXCIsXCJkZXZpY2VJZFwiOm51bGwsXCJzdXBlckFjY291bnRJZFwiOlwiQUNDOTc0NjA1MDU2OTI3MlwiLFwic3RvY2tzQWNjb3VudFN0YXR1c1wiOlwiQ09NUExFVEVEXCJ9IiwibmJmIjoxNjU4MzIwMDg0LCJpc3MiOiJncm93d2JpbGxpb25taWxsZW5uaWFsIiwiZXhwIjoxNjYwOTEyMTM0LCJpYXQiOjE2NTgzMjAxMzR9.cJjcn0JfOQhXEPpUiL7X-0f9vjGacZFrZvBXv6_9KNDNBnEzm6ZAV0-P4rGo1yAH5EVCTVETEsVbP22rpWoQrA" 
    }
    return await stock_controller.get_stocks(name,headersList)

