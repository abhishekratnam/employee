Use a virtual env or whatever means to setup the necessary dependencies such as pipenv.

### install dependencies
pip install -r requirement.txt
### to run app locally
uvicorn main:app --reload

## To navigate to endpoints navigate to http://127.0.0.1:8000/docs# since fastapi already has the swagger support.


#Endpoints supported are below mentioned
| Type | Endpoint   | Notes |
| :---:   | :---: | :---: |
| GET	    |   /company |	Return Company  |
| :---:   | :---: | :---: |
|POST	         |   /company	|Returns the unique company id|
| :---:   | :---: | :---: |
|POST	   |         /employee	|Returns the unique employee id|
| :---:   | :---: | :---: |
GET all employees|	/employee	|Returns the paginated Employees (10 at a time)|


## Setup the POSTGRES DB with the user abhishek and password as password else use the default credentials accordingly

## CREATE database management_portal;
## CREATE user abhishek with encrypted password 'password';
## GRANT ALL privileges on database management_portal to abhishek;

```
CREATE TABLE company (
	id serial4 NOT NULL,
	legal_name varchar(80) NULL,
	incorporation_date varchar(80) NULL,
	display_name varchar(80) NULL,
	us_state_inc varchar(80) NULL,
    CONSTRAINT company_pkey PRIMARY KEY (id)
);

CREATE TABLE employees (
	id serial4 NOT NULL,
	first_name varchar(80) NULL,
	last_name varchar(80) NULL,
	company_id int4 NULL,
	work_email varchar(80) NULL,
	manager_id int4 NULL,
	dob varchar(80) NULL,
	employee_number int4 NULL,
	tax_id int4 NULL,
	employment_status varchar(80) NULL,
	marital_status varchar(80) NULL,
	CONSTRAINT employees_pkey PRIMARY KEY (id)
);

```
<img width="1302" alt="Screenshot 2022-09-10 at 11 12 52 AM" src="https://user-images.githubusercontent.com/24920237/189471396-7c9c29fd-e8f5-4eff-8a32-6b38cd518656.png">
<img width="1302" alt="Screenshot 2022-09-10 at 11 28 33 AM" src="https://user-images.githubusercontent.com/24920237/189471312-6af147b2-8008-4c87-bbea-9b68973567b5.png">
<img width="1302" alt="Screenshot 2022-09-10 at 11 33 42 AM" src="https://user-images.githubusercontent.com/24920237/189471440-c60a5fc9-a547-4b21-8175-bb40baf97d9d.png">
# Logging
<img width="1302" alt="Screenshot 2022-09-10 at 6 39 22 PM" src="https://user-images.githubusercontent.com/24920237/189484823-49706e0f-e93f-421f-854e-032441b59133.png">




