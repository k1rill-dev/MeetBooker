import uuid
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.models import Base
from src.schemas.appointments import AppointmentSchema


class Appointment(Base):
    __tablename__ = 'appointments'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    specialist_id: Mapped[UUID] = mapped_column(ForeignKey('specialists.id'))
    slot_id: Mapped[UUID] = mapped_column(ForeignKey('schedule_slots.id'))
    is_confirmed: Mapped[bool]

    def to_read_model(self) -> AppointmentSchema:
        return AppointmentSchema(
            id=self.id,
            user_id=self.user_id,
            specialist_id=self.specialist_id,
            slot_id=self.slot_id,
            is_confirmed=self.is_confirmed
        )
