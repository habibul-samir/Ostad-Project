from django.urls import path
from .views import AllCourses, AddCourse, DeleteCourse, UpdateCourse

app_name="Courses"

urlpatterns = [
    path('courses/', AllCourses.as_view(), name="all_courses"),
    path('courses/add/', AddCourse.as_view(), name="add_course"), 
    path('courses/<int:pk>/delete/', DeleteCourse.as_view(), name="delete_course"),
    path('courses/<int:pk>/edit/', UpdateCourse.as_view(), name="edit_course"),

]