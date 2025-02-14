from django.urls import path
from .views import AddStudent, AllStudents, DeleteStudent, UpdateStudent, StudentDetails, RemoveStudentCourse

app_name="Students"

urlpatterns = [
    path("students/", AllStudents.as_view(), name="all_students"),
    path("students/add/", AddStudent.as_view(), name="add_student"),
    path("students/<int:pk>/delete/", DeleteStudent.as_view(), name="delete_student"), 
    path('students/<int:pk>/edit/', UpdateStudent.as_view(), name='edit_student'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='student_details'), 
    path('students/<int:pk>/remove_course/<int:cid>/', RemoveStudentCourse.as_view(), name='remove_student_course'),  
]