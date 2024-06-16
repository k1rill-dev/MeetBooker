from abc import ABC, abstractmethod
from typing import Union, TypeVar, Optional
from uuid import UUID

from pydantic import BaseModel, Field
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func

from src.adapters.models import Specialist, User, SpecialistRating
from src.schemas.specialists import JoinedResult

PrimaryKey = TypeVar('PrimaryKey')


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> PrimaryKey:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, pk: UUID, data: dict) -> BaseModel:
        stmt = update(self.model).values(**data).where(self.model.id == pk).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()

    async def find_all(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def join_all(self):
        stmt = (select(
            Specialist.id, func.sum(SpecialistRating.rating).label('sum_rating'),
            Specialist.user_id, User.first_name, User.last_name, User.email, Specialist.bio,
            Specialist.speciality, User.profile_picture)
                .join(User, User.id == Specialist.user_id)
                .join(SpecialistRating, SpecialistRating.specialist_id == Specialist.id)).group_by(Specialist.id,
                                                                                                   User.first_name,
                                                                                                   User.last_name,
                                                                                                   User.email,
                                                                                                   Specialist.bio,
                                                                                                   Specialist.speciality,
                                                                                                   User.profile_picture)
        res = await self.session.execute(stmt)
        # print([u._asdict() for u in res.all()])
        response = [JoinedResult(**u._asdict()) for u in res.all()]
        return response

    async def find_one(self, **filter_by) -> BaseModel:
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res

    async def edit_multiply(self, updated_data: dict, **filter_by):
        stmt = update(self.model).filter_by(**filter_by).values(**updated_data)
        res = await self.session.execute(stmt)
        return res

    async def sum(self, field, **filter_by):
        stmt = select(func.sum(field)).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.all()
