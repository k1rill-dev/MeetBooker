import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.models import Base
from src.schemas.schedule import ScheduleSchema


class ScheduleSlot(Base):
    __tablename__ = 'schedule_slots'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    specialist_id: Mapped[UUID] = mapped_column(ForeignKey('specialists.id'))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    is_booked: Mapped[bool]

    def to_read_model(self) -> ScheduleSchema:
        return ScheduleSchema(
            id=self.id,
            specialist_id=self.specialist_id,
            start_time=self.start_time,
            end_time=self.end_time,
            is_booked=self.is_booked
        )