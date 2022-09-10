from datetime import datetime
from fastapi import FastAPI
from typing import Optional
from database.db import get_db, Employees,Company
from models.employeeModels import Employeesmodel,Companymodel
import requests
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy_future import paginate
from fastapi import Depends, FastAPI, HTTPException
dt = datetime.now()    # for date and time
ts = datetime.timestamp(dt)    # for timestamp
employee = FastAPI()
from config import logger_init
logger = logger_init('api')

@employee.post("/company")
def post_Company(company:Companymodel, db: Session = Depends(get_db)):
    try:
        to_create = Company(
            legal_name = company.legal_name,
            incorporation_date = company.incorporation_date,
            display_name = company.display_name,
            us_state_inc = company.us_state_inc
        )
        db.add(to_create)
        db.commit()
        return {
            "company_id": to_create.id,
            "success":True
        }
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail='There was an error while processing your request.')
     

@employee.post("/employee")
def post_Employee(employee:Employeesmodel, db: Session = Depends(get_db)):
    try:
        to_create = Employees(
        first_name=employee.first_name,
        last_name=employee.last_name,
        company_id=employee.company_id,
        work_email=employee.work_email,
        manager_id=employee.manager_id,
        dob=employee.dob,
        employee_number=employee.employee_number,
        tax_id=employee.tax_id,
        employment_status=employee.employment_status,
        marital_status=employee.marital_status,
        )
        db.add(to_create)
        db.commit()
        return {
            "employee_id": to_create.id,
            "success":True
        }
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail='There was an error while processing your request.')
     
@employee.get("/employee")
async def get_Employee(db: Session = Depends(get_db),page: int = 0):
    try:
        limit = 10
        employees = db.query(Employees).offset(page).limit(limit).all()
        return employees
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail='There was an error while processing your request.')
    
@employee.get("/company")
async def get_Company(db: Session = Depends(get_db),page: int = 0):
    try:
        limit = 10
        company_details = db.query(Company).offset(page).limit(limit).all()
        return company_details
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail='There was an error while processing your request.')
