from sqladmin import ModelView

from src.adapters.models import Appointment


class AppointmentAdmin(ModelView, model=Appointment):
    column_list = [Appointment.id, Appointment.user_id, Appointment.specialist_id, Appointment.slot_id,
                   Appointment.is_confirmed]
    column_labels = {
        Appointment.id: "ID",
        Appointment.user_id: "User ID",
        Appointment.specialist_id: "Specialist ID",
        Appointment.slot_id: "Slot ID",
        Appointment.is_confirmed: "Is Confirmed"
    }
    column_searchable_list = [Appointment.user_id, Appointment.specialist_id]
    column_filters = [Appointment.is_confirmed]
