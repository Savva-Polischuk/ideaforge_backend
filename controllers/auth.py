from litestar import Controller, post
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import data_base_helper, Client


class AuthController(Controller):
    @post(path='/', dependencies={'session': data_base_helper.session_dependency})
    async def check_user(self, email: str, password: str, session: AsyncSession):
        is_authorized = await session.scalar(select(Client).where(
            Client.email == email,
            Client.password == password
        )
        )
        if is_authorized is not None:
            return True
        return False
