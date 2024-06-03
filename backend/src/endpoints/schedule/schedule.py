from uuid import UUID
from fastapi import APIRouter, Depends
from src.endpoints.dependencies import UnitOfWorkDependency, get_user_from_token, get_specialist_from_token
from src.schemas.appointments import AppointmentSchema
from src.schemas.schedule import ScheduleSchema
from src.schemas.user import UserSchema
from src.service.db_services.appointment_service import AppointmentService
from src.service.db_services.schedule_service import ScheduleService

schedule_routes = APIRouter(tags=["Schedule"])


@schedule_routes.get("/appointment")
async def get_appointment(uow: UnitOfWorkDependency, user: UserSchema = Depends(get_user_from_token)):
    """
    Возвращает все брони пользователя
    :param uow:
    :param user:
    :return:
    """
    appointment = await AppointmentService().list(uow=uow, user_id=user.id)
    return appointment


@schedule_routes.post("/schedule")
async def create_schedule(uow: UnitOfWorkDependency, schedule: ScheduleSchema,
                          user: UserSchema = Depends(get_specialist_from_token)):
    """
    создает новый слот расписания у специалиста
    :param uow:
    :param schedule:
    :param user:
    :return:
    """
    schedule.specialist_id = user.id
    slot = await ScheduleService().add(uow=uow, data=schedule)
    return slot


@schedule_routes.get("/schedule/{specialist_id}")
async def get_schedule(uow: UnitOfWorkDependency, specialist_id: UUID):
    """
    получает все расписания текущего специлиста
    :param uow:
    :param specialist_id:
    :return:
    """
    schedule = await ScheduleService().list(uow=uow, specialist_id=specialist_id)
    return schedule


@schedule_routes.put("/schedule/{schedule_id}")
async def update_schedule(uow: UnitOfWorkDependency, schedule_id: UUID, schedule: ScheduleSchema,
                          user: UserSchema = Depends(get_specialist_from_token)):
    """
    редактирование расписания
    :param uow:
    :param schedule_id:
    :param schedule:
    :param user:
    :return:
    """
    schedule.specialist_id = user.id
    res = await ScheduleService().edit(uow=uow, pk=schedule_id, data=schedule)
    return res


@schedule_routes.post("/appointment", dependencies=[Depends(get_user_from_token), ])
async def create_appointment(uow: UnitOfWorkDependency, appointment_data: AppointmentSchema):
    appointment = await AppointmentService().add(uow=uow, data=appointment_data)
    return appointment


@schedule_routes.put("/appointment/{appointment_id}")
async def update_appointment(uow: UnitOfWorkDependency, appointment_id: UUID, appointment_data: AppointmentSchema,
                             user: UserSchema = Depends(get_user_from_token)):
    appointment = await AppointmentService().edit(uow=uow, pk=appointment_id, data=appointment_data)
    return appointment
