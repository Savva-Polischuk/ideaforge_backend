from pydantic import BaseModel


class ProjectEmploymentModel(BaseModel):
    project_id: int
    employee_id: int
