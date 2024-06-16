from abc import ABC, abstractmethod
from datetime import datetime
from typing import Union, TypeVar, Optional
from uuid import UUID

from pydantic import BaseModel, Field
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func

from src.adapters.models import Specialist, User, SpecialistRating, Appointment, ScheduleSlot
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

    async def delete_one(self, pk: UUID):
        stmt = delete(self.model).where(self.model.id == pk)
        res = await self.session.execute(stmt)
        return res

    async def join_all(self, **filter_by):
        stmt = ((select(
            Specialist.id, func.sum(SpecialistRating.rating).label('sum_rating'),
            Specialist.user_id, User.first_name, User.last_name, User.email, Specialist.bio,
            Specialist.speciality, User.profile_picture)
                 .join(User, User.id == Specialist.user_id)
                 .join(SpecialistRating, SpecialistRating.specialist_id == Specialist.id)).filter_by(
            **filter_by).group_by(Specialist.id,
                                  User.first_name,
                                  User.last_name,
                                  User.email,
                                  Specialist.bio,
                                  Specialist.speciality,
                                  User.profile_picture))
        res = await self.session.execute(stmt)
        response = [JoinedResult(**u._asdict()) for u in res.all()]
        return response

    async def join_all_appointments(self, specialist_id: Optional[UUID] = None, user_id: Optional[UUID] = None):
        class AppointmentSchema(BaseModel):
            id: UUID = Field(alias='id')
            user_first_name: str
            user_last_name: str
            specialist_first_name: str
            specialist_last_name: str
            slot_start_time: datetime
            slot_end_time: datetime
            is_confirmed: bool

        stmt = select(Appointment)
        if specialist_id and not user_id:
            stmt = stmt.filter(Appointment.specialist_id == specialist_id)
        if user_id and not specialist_id:
            stmt = stmt.filter(Appointment.user_id == user_id)

        stmt = stmt.join(User, Appointment.user_id == User.id)
        stmt = stmt.join(Specialist, Appointment.specialist_id == Specialist.id)
        stmt = stmt.join(ScheduleSlot, Appointment.slot_id == ScheduleSlot.id)

        stmt = stmt.options(
            joinedload(Appointment.user),
            joinedload(Appointment.specialist),
            joinedload(Appointment.slot)
        )

        res = await self.session.execute(stmt)
        appointment_schemas = [
            AppointmentSchema(
                id=appointment.id,
                user_first_name=appointment.user.first_name,
                user_last_name=appointment.user.last_name,
                specialist_first_name=appointment.specialist.user.first_name,
                specialist_last_name=appointment.specialist.user.last_name,
                slot_start_time=appointment.slot.start_time,
                slot_end_time=appointment.slot.end_time,
                is_confirmed=appointment.is_confirmed,
            )
            for appointment in res.scalars().all()
        ]
        return appointment_schemas

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
