from asyncio import current_task
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession

from settings import DB_NAME, DB_HOST, DB_PASSWORD, DB_USERNAME

url_db = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


class DataBaseHelper:
    def __init__(self, url: str):
        self.engin = create_async_engine(
            url=url,
            echo=False
        )
        self.session_factory = async_sessionmaker(
            bind=self.engin,
            autoflush=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        # async with self.get_scoped_session() as session:
        session = self.get_scoped_session()
        yield session
        await session.remove()


engine = create_async_engine(url=url_db)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


data_base_helper = DataBaseHelper(url_db)
