from database.db import Base, engine
from models.stockModels import Stocks

print("Creating DataBase")

Base.metadata.create_all(engine)