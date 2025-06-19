from pydantic import BaseModel


class DepartmentModel(BaseModel):
    name: str
