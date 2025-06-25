from datetime import date
from pydantic import BaseModel, EmailStr, ConfigDict


class EmployeeModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    department_id: int
    name: str
    surname: str
    middlename: str
    salary: int
    hire_date: date


class ClientModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    surname: str
    password: str
    email: EmailStr


class DepartmentModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str


class ProjectModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    client_id: int
    name: str
    description: str
    stage: str
    progress: int
    completion: date | None


class ProjectEmploymentModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    project_id: int
    employee_id: int
