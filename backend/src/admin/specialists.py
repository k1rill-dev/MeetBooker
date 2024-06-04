from sqladmin import ModelView

from src.adapters.models import Specialist, SpecialistRating


class SpecialistAdmin(ModelView, model=Specialist):
    column_list = [Specialist.id, Specialist.speciality, Specialist.bio, Specialist.user_id]
    column_labels = {
        Specialist.id: "ID",
        Specialist.speciality: "Speciality",
        Specialist.bio: "Bio",
        Specialist.user_id: "User ID"
    }
    column_searchable_list = [Specialist.speciality, Specialist.bio]
    column_filters = [Specialist.speciality]


class SpecialistRatingAdmin(ModelView, model=SpecialistRating):
    column_list = [SpecialistRating.id, SpecialistRating.user_id, SpecialistRating.specialist_id,
                   SpecialistRating.rating]
    column_labels = {
        SpecialistRating.id: "ID",
        SpecialistRating.user_id: "User ID",
        SpecialistRating.specialist_id: "Specialist ID",
        SpecialistRating.rating: "Rating"
    }
    column_searchable_list = [SpecialistRating.user_id, SpecialistRating.specialist_id]
    column_filters = [SpecialistRating.rating]
