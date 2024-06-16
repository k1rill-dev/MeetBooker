from typing import Any, Optional
from uuid import UUID

from src.schemas.appointments import AppointmentSchema, UpdateAppointmentSchema, CreateAppointmentSchema
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class AppointmentService(AbstractService):
    async def add(self, uow: IUnitOfWork, data: AppointmentSchema):
        async with uow:
            res = await uow.appointments.add_one(data=data.model_dump())
            await uow.commit()
            return res

    async def joined_list(self, uow: IUnitOfWork, specialist_id: Optional[UUID] = None, user_id: Optional[UUID] = None):
        async with uow:
            if specialist_id:
                res = await uow.appointments.join_all_appointments(specialist_id=specialist_id)
                return res
            elif not specialist_id and user_id:
                res = await uow.appointments.join_all_appointments(user_id=user_id)
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
