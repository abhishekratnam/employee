from email.policy import default
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import uuid

# # SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
SQLALCHEMY_DATABASE_URL = "postgresql://abhishek:password@postgresserver/stocks_watcher"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
    

def generate_uuid():
    return str(uuid.uuid4())
Base = declarative_base()
class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True, default=generate_uuid)
    name = Column(String)
    type = Column(String)
    open = Column(float)
    high = Column(float)
    low = Column(float)
    close = Column(float)
    ltp = Column(float)
    volume = Column(float)
    lowPriceRange = Column(float)
    highPriceRange = Column(float)
    day_change_percent = Column(float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "created": self.time_created
        }

# class Fundamentals(Base):
#     __tablename__ = "fundamentals"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     # pe_ratio = Column(float)
#     # pb_ratio = Column(float)
#     # market_cap = Column(float)
#     # book_value = Column(float)
#     # eps_ttm = Column(float)
#     # roe = Column(float)
#     # industry_pe = Column(float)
#     capped_type = Column(String)
#     # dividend_yield_percent = Column(float)
#     # debt_to_equity = Column(float)
#     face_value =  Column(Integer)
#     fundamentals = relationship("stock")
#     class Config:
#         orm_mode = True


