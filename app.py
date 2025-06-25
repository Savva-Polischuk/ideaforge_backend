from logging import DEBUG

from litestar import Litestar, get, post
from litestar.di import Provide
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.config.cors import CORSConfig

from CRUD.models import ClientModel, ProjectModel
from database import Client, Project, get_async_session
from controllers import AdminController


@post(path='/', dependencies={'session': Provide(get_async_session)})
async def check_user(email: str, password: str, session: AsyncSession) -> bool | dict[str, str | int]:
    authorized = await session.scalar(select(Client).where(
            Client.email == email,
            Client.password == password
        )
    )
    print(authorized)
    if authorized is not None:
        return {'client_id': authorized.id, 'name': authorized.name}
    return False


@get(path='/profile', dependencies={'session': Provide(get_async_session)})
async def get_user_projects(client_id: int, session: AsyncSession) -> list[ProjectModel]:
    print(session is None)
    res = await session.scalars(select(Project).where(Project.client_id == int(client_id)))
    print(res is None)
    return [ProjectModel.model_validate(c) for c in res.all()]


cors_config = CORSConfig(allow_origins=["*"])

app = Litestar(route_handlers=[check_user, get_user_projects, AdminController], cors_config=cors_config)
app.get_logger().setLevel(DEBUG)
