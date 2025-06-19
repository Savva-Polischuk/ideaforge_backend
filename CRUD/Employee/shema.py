from pydantic import BaseModel
from datetime import date


class EmployeeModel(BaseModel):
    department_id: int
    name: str
    surname: str
    middlename: str
    salary: int
    hire_date: date


