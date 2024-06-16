from uuid import UUID
from fastapi import APIRouter, Depends
from src.endpoints.dependencies import UnitOfWorkDependency, get_user_from_token, get_specialist_from_token
from src.schemas.appointments import CreateAppointmentSchema, UpdateAppointmentSchema
from src.schemas.schedule import ScheduleSchema, CreateScheduleSchema, UpdateScheduleSchema
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
    print(user)
    appointment = await AppointmentService().joined_list(uow=uow, user_id=user.id)
    return appointment


@schedule_routes.get("/spec-appointment")
async def get_specialist_appointment(uow: UnitOfWorkDependency, user: UserSchema = Depends(get_specialist_from_token)):
    """
    Возвращает все брони специалиста
    :param uow:
    :param user:
    :return:
    """
    appointment = await AppointmentService().joined_list(uow=uow, specialist_id=user.id)
    return appointment


@schedule_routes.post("/schedule")
async def create_schedule(uow: UnitOfWorkDependency, schedule: CreateScheduleSchema,
                          user: UserSchema = Depends(get_specialist_from_token)):
    """
    создает новый слот расписания у специалиста
    :param uow:
    :param schedule:
    :param user:
    :return:
    """
    schedule.specialist_id = user.id
    schedule.start_time = schedule.start_time.replace(tzinfo=None)
    schedule.end_time = schedule.end_time.replace(tzinfo=None)
    slot = await ScheduleService().add(uow=uow, data=schedule)
    return slot


@schedule_routes.delete("/schedule/{schedule_id}")
async def delete_schedule(uow: UnitOfWorkDependency, schedule_id: UUID,
                          user: UserSchema = Depends(get_specialist_from_token)):
    """
    удаляет слот расписания
    :param uow:
    :param schedule_id:
    :return:
    """
    res = await ScheduleService().delete_one(uow, schedule_id)
    return res


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


@schedule_routes.patch("/schedule/{schedule_id}")
async def update_schedule(uow: UnitOfWorkDependency, schedule_id: UUID, schedule: UpdateScheduleSchema,
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
    if schedule.start_time is not None:
        schedule.start_time = schedule.start_time.replace(tzinfo=None)
    if schedule.end_time is not None:
        schedule.end_time = schedule.end_time.replace(tzinfo=None)
    res = await ScheduleService().edit(uow=uow, pk=schedule_id, data=schedule)
    return res


@schedule_routes.post("/appointment", dependencies=[Depends(get_user_from_token), ])
async def create_appointment(uow: UnitOfWorkDependency, appointment_data: CreateAppointmentSchema):
    appointment = await AppointmentService().add(uow=uow, data=appointment_data)
    return appointment


@schedule_routes.patch("/appointment/{appointment_id}")
async def update_appointment(uow: UnitOfWorkDependency, appointment_id: UUID, appointment_data: UpdateAppointmentSchema,
                             user: UserSchema = Depends(get_user_from_token)):
    appointment = await AppointmentService().edit(uow=uow, pk=appointment_id, data=appointment_data)
    return appointment
