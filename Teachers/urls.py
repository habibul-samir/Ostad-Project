from django.urls import path
from .views import AddTeacher, AllTeachers, UpdateTeacher, DeleteTeacher

app_name="Teachers"

urlpatterns = [
    path("teachers/add/", AddTeacher.as_view(), name="add_teacher"),
    path("teachers/", AllTeachers.as_view(), name="all_teachers"),
    path("teachers/<int:pk>/edit/", UpdateTeacher.as_view(), name="edit_teacher"),
    path("teachers/<int:pk>/delete/", DeleteTeacher.as_view(), name="delete_teacher"),

]