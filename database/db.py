from email.policy import default
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import func
import uuid
SQLALCHEMY_DATABASE_URL = "postgresql://abhishek:password@localhost/management_portal"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
from config import logger_init
logger = logger_init('database')


Base = declarative_base()
def get_db():
    db= SessionLocal()
    try:
        yield db
    except:
        logger.error("Closed DB unexpectedly")
        db.close()


def generate_uuid():
    return str(uuid.uuid4())   

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    legal_name = Column(String)
    incorporation_date = Column(DateTime(timezone=True), server_default=func.now())
    display_name = Column(String)
    us_state_inc = Column(String) # (For example: California)

class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    first_name          = Column(String)
    last_name           = Column(String)
    company_id          = Column(Integer)
    work_email          = Column(String)
    manager_id          = Column(Integer)
    dob                 = Column(String)
    employee_number     = Column(Integer)
    tax_id              = Column(Integer)
    employment_status   = Column(String)#One of ACTIVE and INACTIVE
    marital_status      = Column(String)