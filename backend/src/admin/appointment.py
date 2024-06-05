from sqladmin import ModelView

from src.adapters.models import Appointment


class AppointmentAdmin(ModelView, model=Appointment):
    column_list = [Appointment.id, Appointment.user, Appointment.specialist_id, Appointment.slot,
                   Appointment.is_confirmed]
    column_labels = {
        Appointment.id: "ID",
        Appointment.user: "User ID",
        Appointment.specialist: "Specialist ID",
        Appointment.slot: "Slot ID",
        Appointment.is_confirmed: "Is Confirmed"
    }
    column_searchable_list = [Appointment.user, Appointment.specialist]
    column_filters = [Appointment.is_confirmed]
    form_columns = [Appointment.id, Appointment.user, Appointment.specialist_id, Appointment.slot,
                   Appointment.is_confirmed]