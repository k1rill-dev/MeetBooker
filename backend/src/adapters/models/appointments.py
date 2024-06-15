import uuid
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.models import Base
from src.schemas.appointments import AppointmentSchema


class Appointment(Base):
    __tablename__ = 'appointments'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    specialist_id: Mapped[UUID] = mapped_column(ForeignKey('specialists.id', ondelete='CASCADE'))
    slot_id: Mapped[UUID] = mapped_column(ForeignKey('schedule_slots.id', ondelete='CASCADE'))
    is_confirmed: Mapped[bool]

    user = relationship("User", foreign_keys=[user_id], backref="appointments", lazy="selectin",
                        cascade="all, delete")
    specialist = relationship("Specialist", foreign_keys=[specialist_id], backref="appointments", lazy="selectin",
                        cascade="all, delete")
    slot = relationship("ScheduleSlot", foreign_keys=[slot_id], backref="appointments", lazy="selectin",
                        cascade="all, delete")

    def __str__(self):
        return str(self.user)

    def to_read_model(self) -> AppointmentSchema:
        return AppointmentSchema(
            id=self.id,
            user_id=self.user_id,
            specialist_id=self.specialist_id,
            slot_id=self.slot_id,
            is_confirmed=self.is_confirmed
        )
