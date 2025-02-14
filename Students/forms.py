from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'student name'}),
            'email_address': forms.EmailInput(attrs={'placeholder': 'student Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'student Phone Number'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }