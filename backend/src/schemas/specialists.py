from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BaseSpecialistSchema(BaseModel):
    speciality: str
    bio: str
    user_id: UUID

    class Config:
        from_attributes = True


class SpecialistSchema(BaseSpecialistSchema):
    id: UUID


class CreateSpecialistSchema(BaseSpecialistSchema):
    pass


class UpdateSpecialistSchema(BaseSpecialistSchema):
    speciality: Optional[str] = None
    bio: Optional[str] = None
    user_id: UUID = None


class BaseSpecialistRatingSchema(BaseModel):
    user_id: UUID
    specialist_id: UUID
    rating: float

    class Config:
        from_attributes = True


class SpecialistRatingSchema(BaseSpecialistRatingSchema):
    id: UUID


class CreateSpecialistRatingSchema(BaseSpecialistRatingSchema):
    pass
