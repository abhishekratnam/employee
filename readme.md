Use a virtual env or whatever means to setup the necessary dependencies such as pipenv.

###install dependencies
pip install -r requirement.txt
###to run app locally
uvicorn main:app --reload
To navigate to endpoints goto http://127.0.0.1:8000/docs# since fastapi already has the swagger support


Endpoints supported are below mentioned

Type	            Endpoint        Notes
GET	                /company	Return Company
POST	            /company	Returns the unique company id
POST	            /employee	Returns the unique employee id
GET all employees	/employee	Returns the paginated Employees (10 at a time)


#Setup the DB with the user abhishek and password as 'password' else use the default credentials accordingly

CREATE database management_portal;
CREATE user abhishek with encrypted password 'password';
GRANT ALL privileges on database management_portal to abhishek;

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