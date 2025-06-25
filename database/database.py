from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column, relationship)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")


class Client(Base):
    __tablename__ = 'client'

    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]


class Project(Base):
    __tablename__ = 'project'

    client_id: Mapped[int] = mapped_column(ForeignKey(Client.id))
    name: Mapped[str]
    description: Mapped[str]
    stage: Mapped[str]
    progress: Mapped[int]
    completion: Mapped[date | None]


class Department(Base):
    __tablename__ = 'department'

    name: Mapped[str]


class Employee(Base):
    __tablename__ = 'employee'

    department_id: Mapped[int] = mapped_column(ForeignKey(Department.id))
    name: Mapped[str]
    surname: Mapped[str]
    middlename: Mapped[str]
    salary: Mapped[int]
    hire_date: Mapped[date]
    department: Mapped["Department"] = relationship(lazy="joined")


class ProjectEmployment(Base):
    __tablename__ = 'project_employment'

    project_id: Mapped[int] = mapped_column(ForeignKey(Project.id))
    employee_id: Mapped[int] = mapped_column(ForeignKey(Employee.id))
