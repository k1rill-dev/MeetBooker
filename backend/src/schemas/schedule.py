from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class ScheduleSchema(BaseModel):
    id: UUID
    specialist_id: UUID
    start_time: datetime
    end_time: datetime
    is_booked: bool

    class Config:
        from_attributes = True
