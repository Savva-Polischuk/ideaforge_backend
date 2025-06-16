from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship)
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from typing import List
from pydantic import EmailStr


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")



