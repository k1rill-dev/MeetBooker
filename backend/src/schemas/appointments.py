from uuid import UUID
from pydantic import BaseModel


class AppointmentSchema(BaseModel):
    id: UUID
    user_id: UUID
    specialist_id: UUID
    slot_id: UUID
    is_confirmed: bool

    class Config:
        from_attributes = True
