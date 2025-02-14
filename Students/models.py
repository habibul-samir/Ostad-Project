from django.db import models
import os
from Courses.models import Course

# Create your models here.

def student_directory_path(instance, filename): 
    return os.path.join(f"Students/media/{instance.name}-{instance.id}", filename)
  
class Student(models.Model):

    name = models.CharField(max_length=100)
    gender_choices = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=6, choices=gender_choices)
    date_of_birth = models.DateField()
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    # photo = models.ImageField(upload_to=student_directory_path, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name="students", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
