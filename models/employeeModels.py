from datetime import datetime
from pydantic import BaseModel
class Employeesmodel(BaseModel):
    first_name          :str
    last_name           :str
    company_id          :int
    work_email          :str
    manager_id          :int
    dob                 :str
    employee_number     :int
    tax_id              :int
    employment_status   :str
    marital_status      :str
    class Config:
        orm_mode = True

class Companymodel(BaseModel):
    legal_name :str    
    incorporation_date:str    
    display_name : str    
    us_state_inc :str     

    class Config:
        orm_mode = True


