from sqlalchemy import select, update, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import ClientModel


async def create(client_in: ClientModel, session: AsyncSession):
    pass

async def read(data, session: AsyncSession):
    pass

async def update(client_in: ClientModel, session: AsyncSession):
    pass

async def delete(data, session: AsyncSession):
    pass