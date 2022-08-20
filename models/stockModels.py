from pydantic import BaseModel
class Stocks(BaseModel):
    name:str
    type:str
    open:float
    high:float
    low:float
    close:float
    ltp:float
    volume:float
    lowPriceRange:float
    highPriceRange:float
    dayChange:float
    dayChangePerc:float
    class Config:
        orm_mode = True
