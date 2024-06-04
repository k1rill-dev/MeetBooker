from typing import Any
from uuid import UUID

from src.schemas.appointments import AppointmentSchema, UpdateAppointmentSchema, CreateAppointmentSchema
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class AppointmentService(AbstractService):
    async def add(self, uow: IUnitOfWork, data: CreateAppointmentSchema):
        async with uow:
            res = await uow.appointments.add_one(data=data.model_dump())
            await uow.commit()
            return res

    async def list(self, uow: IUnitOfWork, **filter_by: Any):
        async with uow:
            res = await uow.appointments.find_all(**filter_by)
            return res

    async def edit(self, uow: IUnitOfWork, pk: UUID, data: UpdateAppointmentSchema):
        async with uow:
            res = await uow.appointments.edit_one(pk=pk, data=data.dict(exclude_none=True))
            await uow.commit()
            return res
