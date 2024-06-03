from uuid import UUID
from fastapi import APIRouter, Depends
from src.endpoints.dependencies import UnitOfWorkDependency, get_user_from_token
from src.schemas.specialists import SpecialistSchema, SpecialistRatingSchema
from src.schemas.user import UserSchema
from src.service.db_services.specialist_service import SpecialistService, SpecialistRatingService

specialists_router = APIRouter(tags=["specialists"])


@specialists_router.get("/specialist")
async def get_all_specialists(uow: UnitOfWorkDependency):
    return SpecialistService().list(uow=uow)


@specialists_router.post("/")
async def create_specialist(uow: UnitOfWorkDependency, spec: SpecialistSchema):
    specialist = await SpecialistService().add(uow, spec)
    return specialist


@specialists_router.get("/specialist/{id}")
async def get_specialist(id: UUID, uow: UnitOfWorkDependency):
    specialist = await SpecialistService().get(id, uow)
    rating = await SpecialistRatingService().list(uow=uow, id=id)
    return dict(specialist=specialist, raiting=rating)


@specialists_router.patch("/specialist")
async def update_specialist(uow: UnitOfWorkDependency,
                            spec_data: SpecialistSchema,
                            user: UserSchema = Depends(get_user_from_token)):
    spec_id = await SpecialistService().get(spec_data.id, uow)
    specialist = await SpecialistService().update(uow=uow, pk=spec_id.id, data=spec_data)
    return specialist


@specialists_router.post("/specialist-rating")
async def set_specialist_rating(uow: UnitOfWorkDependency, rating_data: SpecialistRatingSchema,
                                user: UserSchema = Depends(get_user_from_token)):
    rating = await SpecialistRatingService().add(uow, rating_data)
    return rating
