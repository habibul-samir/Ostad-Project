from django import forms
from .models import Course

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = "__all__"

        widgets = {
            'course_code': forms.TextInput(attrs={'placeholder': 'Course Code'}),
            'course_name': forms.TextInput(attrs={'placeholder': 'Course Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Course Description'}),
 
        }