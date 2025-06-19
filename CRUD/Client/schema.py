from pydantic import BaseModel, EmailStr


class ClientModel(BaseModel):
    name: str
    surname: str
    password: str
    email: EmailStr
