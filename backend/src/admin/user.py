from sqladmin import ModelView

from src.adapters.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.first_name, User.last_name, User.is_active, User.is_superuser,
                   User.profile_picture]
    column_labels = {
        User.id: "ID",
        User.email: "Email",
        User.first_name: "First Name",
        User.last_name: "Last Name",
        User.is_active: "Is Active",
        User.is_superuser: "Is Superuser",
        User.profile_picture: "Profile Picture"
    }
    column_searchable_list = [User.email, User.first_name, User.last_name]
    column_filters = [User.is_active, User.is_superuser]
    form_columns = [User.email, User.first_name, User.last_name, User.is_active, User.is_superuser,
                    User.profile_picture]
