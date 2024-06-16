from typing import Any
from uuid import UUID

from sqlalchemy.exc import NoResultFound

from src.adapters.models import SpecialistRating
from src.adapters.repository import PrimaryKey
from src.schemas.specialists import SpecialistSchema, CreateSpecialistSchema, UpdateSpecialistSchema
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class SpecialistService(AbstractService):
    async def add(self, uow: IUnitOfWork, data: SpecialistSchema) -> PrimaryKey:
        async with uow:
            spec = await uow.specialist.add_one(data=data.model_dump())
            await uow.commit()
            return spec

    async def list(self, uow: IUnitOfWork, **filter_by: Any):
        async with uow:
            res = await uow.specialist.find_all(**filter_by)
            return res

    async def joined_list(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.specialist.join_all()
            return res

    async def get(self, id: UUID, uow: IUnitOfWork):
        async with uow:
            spec = await uow.specialist.find_one(id=id)
            return spec

    async def get_by_user_id(self, user_id: UUID, uow: IUnitOfWork):
        async with uow:
            spec = await uow.specialist.find_one(user_id=user_id)
            return spec

    async def update(self, uow: IUnitOfWork, pk: UUID, data: UpdateSpecialistSchema):
        async with uow:
            spec = await uow.specialist.edit_one(pk=pk, data=data.dict(exclude_none=True))
            await uow.commit()
            return spec


class SpecialistRatingService(AbstractService):
    async def add(self, uow: IUnitOfWork, data):
        async with uow:
            rating = await uow.specialist_ratings.add_one(data=data.model_dump())
            await uow.commit()
            return rating

    async def list(self, uow: IUnitOfWork, **filter_by: Any):
        async with uow:
            try:
                ratings = await uow.specialist_ratings.sum(SpecialistRating.rating, **filter_by)
                return ratings[0]
            except NoResultFound:
                return {
                    "detail": "No specialist ratings found"
                }
