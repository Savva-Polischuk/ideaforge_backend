from pydantic import BaseModel
from datetime import date


class ProjectModel(BaseModel):
    client_id: int
    name: str
    description: str
    stage: str
    progress: int
    completion: date | None
