# ais/forms.py
from django import forms
from .models.students import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['nim', 'name', 'email', 'phone_number', 'year', 'teacher']