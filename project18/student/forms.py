from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','age']
        
    def clean_age(self):

        age = self.cleaned_data['age']

        if age < 18:
            raise forms.ValidationError(
                "Age must be 18 or above."
            )

        return age