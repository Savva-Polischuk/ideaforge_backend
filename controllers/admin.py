from litestar import Controller, get
from litestar.di import Provide
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.models import ClientModel, ProjectModel, EmployeeModel, DepartmentModel, ProjectEmploymentModel
from database import get_async_session, Client, Project, Employee, Department, ProjectEmployment


class AdminController(Controller):
    path = "/admin"

    @get(path='/project', dependencies={'session': Provide(get_async_session)})
    async def get_projects(self, session: AsyncSession) -> list[ProjectModel]:
        res = await session.scalars(select(Project))
        return [ProjectModel.model_validate(c) for c in res.all()]

    @get(path='/employee', dependencies={'session': Provide(get_async_session)})
    async def get_employees(self, session: AsyncSession) -> list[EmployeeModel]:
        res = await session.scalars(select(Employee))
        return [EmployeeModel.model_validate(c) for c in res.all()]

    @get(path='/department', dependencies={'session': Provide(get_async_session)})
    async def get_departments(self, session: AsyncSession) -> list[DepartmentModel]:
        res = await session.scalars(select(Department))
        return [DepartmentModel.model_validate(c) for c in res.all()]

    @get(path='/client', dependencies={'session': Provide(get_async_session)})
    async def get_clients(self, session: AsyncSession) -> list[ClientModel]:
        res = await session.scalars(select(Client))
        return [ClientModel.model_validate(c) for c in res.all()]

    @get(path='/project_employment', dependencies={'session': Provide(get_async_session)})
    async def get_project_employments(self, session: AsyncSession) -> list[ProjectEmploymentModel]:
        res = await session.scalars(select(ProjectEmployment))
        return [ProjectEmploymentModel.model_validate(c) for c in res.all()]

    @get(path='/employee_from_department', dependencies={'session': Provide(get_async_session)})
    async def get_employee_from_department(self, department_id: int, session: AsyncSession) -> list[EmployeeModel]:
        res = await session.scalars(select(Employee).where(Employee.department_id == department_id))
        return [EmployeeModel.model_validate(c) for c in res.all()]

    @get(path='/employee_from_project', dependencies={'session': Provide(get_async_session)})
    async def get_employee_from_project(self, project_id: int, session: AsyncSession) -> list[EmployeeModel]:
        res = await session.scalars(select(Employee).join(ProjectEmployment).where(ProjectEmployment.project_id == project_id))
        return [EmployeeModel.model_validate(c) for c in res.all()]
