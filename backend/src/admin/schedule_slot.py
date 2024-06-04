from sqladmin import ModelView

from src.adapters.models import ScheduleSlot


class ScheduleSlotAdmin(ModelView, model=ScheduleSlot):
    column_list = [ScheduleSlot.id, ScheduleSlot.specialist_id, ScheduleSlot.start_time, ScheduleSlot.end_time,
                   ScheduleSlot.is_booked]
    column_labels = {
        ScheduleSlot.id: "ID",
        ScheduleSlot.specialist_id: "Specialist ID",
        ScheduleSlot.start_time: "Start Time",
        ScheduleSlot.end_time: "End Time",
        ScheduleSlot.is_booked: "Is Booked"
    }
    column_searchable_list = [ScheduleSlot.specialist_id]
    column_filters = [ScheduleSlot.start_time, ScheduleSlot.end_time, ScheduleSlot.is_booked]
