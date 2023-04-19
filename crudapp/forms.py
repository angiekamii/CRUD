from django import forms
from crudapp.models import Student


class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'Email']
