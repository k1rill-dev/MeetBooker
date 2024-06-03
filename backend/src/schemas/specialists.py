from uuid import UUID

from pydantic import BaseModel


class SpecialistSchema(BaseModel):
    id: UUID
    speciality: str
    bio: str
    user_id: UUID

    class Config:
        from_attributes = True


