from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base


class CrudOperations:
    def __init__(self, Table: Base, Model: BaseModel):
        self.Table = Table
        self.Model = Model

    async def create(self, data_in: Model, session: AsyncSession) -> self.Table:
        data_out = self.Table(**data_in.model_dump())
        session.add(data_out)
        await session.commit()
        return data_out

    async def read(self, session: AsyncSession):
        stmt = select(self.Table)
        res = await session.execute(stmt)
        return res.unique().scalars().all()

    async def update(self, data_in: Table, session: AsyncSession) -> None:
        stmt = update(self.Table).where(self.Table.id == data_in.id).values(data_in)
        await session.execute(stmt)
        await session.commit()
