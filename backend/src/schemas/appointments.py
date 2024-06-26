import uuid
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class AppointmentBase(BaseModel):
    user_id: UUID
    specialist_id: UUID
    slot_id: UUID
    is_confirmed: bool

    class Config:
        from_attributes = True


class AppointmentSchema(AppointmentBase):
    id: UUID = Field(default_factory=uuid.uuid4)


class CreateAppointmentSchema(AppointmentBase):
    pass


class UpdateAppointmentSchema(AppointmentBase):
    user_id: Optional[UUID] = None
    specialist_id: Optional[UUID] = None
    slot_id: Optional[UUID] = None
    is_confirmed: Optional[bool] = None
