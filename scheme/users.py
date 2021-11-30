from databases import Database
import datetime
from typing import List, Optional
from db.models import users
from scheme.scheme import User


class BaseRepository:
    def __init__(self, database: Database):
        self.database = database


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_all_by_name(self, name: str, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().where(users.c.name == name).limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_all_by_patronymic(self, patronymic: str, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().where(users.c.patronymic == patronymic).limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_all_by_surname(self, surname: str, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().where(users.c.surname == surname).limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: User) -> User:
        query = users.select().where(users.c.email == u.email)
        if await self.database.fetch_one(query):
            return None
        user = User(
            name=u.name,
            patronomyc=u.patronymic,
            surname=u.surname,
            email=u.email,
            password=u.password,
            when=datetime.datetime.utcnow(),
            update=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, id: int, u: User) -> User:
        query = users.select().where(users.c.email == u.email)
        if await self.database.fetch_one(query):
            return None
        user = User(
            name=u.name,
            patronomyc=u.patronymic,
            surname=u.surname,
            email=u.email,
            password=u.password,
            update=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("when", None)
        values.pop("id", None)
        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)
        return user

    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def delete(self, id: int):
        query = users.delete().where(users.c.id == id)
        return await self.database.execute(query=query)
