import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.models import Base
from src.schemas.schedule import ScheduleSchema


class ScheduleSlot(Base):
    __tablename__ = 'schedule_slots'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    specialist_id: Mapped[UUID] = mapped_column(ForeignKey('specialists.id', ondelete='CASCADE'))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    is_booked: Mapped[bool]

    specialist = relationship("Specialist", foreign_keys=[specialist_id], backref="schedule_slots", lazy="selectin",
                              cascade="all, delete")

    def __str__(self):
        return str(str(self.start_time) + "-" + str(self.end_time))

    def to_read_model(self) -> ScheduleSchema:
        return ScheduleSchema(
            id=self.id,
            specialist_id=self.specialist_id,
            start_time=self.start_time,
            end_time=self.end_time,
            is_booked=self.is_booked
        )
