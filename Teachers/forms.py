from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = "__all__"

        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Teacher name'}),
            'email_address': forms.EmailInput(attrs={'placeholder': 'Tacher Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Teacher Phone Number'}),
            'designation': forms.TextInput(attrs={'placeholder': 'Teacher Designation'}),
            
        }