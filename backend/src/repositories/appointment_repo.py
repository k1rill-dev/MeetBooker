from src.adapters.models import Appointment
from src.adapters.repository import SQLAlchemyRepository


class AppointmentRepository(SQLAlchemyRepository):
    model = Appointment
