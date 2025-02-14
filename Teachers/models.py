from django.db import models
from Courses.models import Course
import os

# Create your models here.

def teacher_directory_path(instance, filename): 
    return os.path.join(f"Teachers/media/{instance.fullname}-{instance.id}", filename)

class Teacher(models.Model):
    fullname = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, related_name="teachers", blank=True, null=True)
    # photo = models.ImageField(upload_to=teacher_directory_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.fullname
