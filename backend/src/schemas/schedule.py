import uuid
from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field


class BaseScheduleSchema(BaseModel):
    specialist_id: UUID
    start_time: datetime
    end_time: datetime
    is_booked: bool

    class Config:
        from_attributes = True


class ScheduleSchema(BaseScheduleSchema):
    id: UUID = Field(default_factory=uuid.uuid4)


class CreateScheduleSchema(BaseScheduleSchema):
    specialist_id: UUID = None


class UpdateScheduleSchema(BaseScheduleSchema):
    specialist_id: Optional[UUID] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    is_booked: Optional[bool] = None
