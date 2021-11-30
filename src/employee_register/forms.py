from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname':'სახელი',
            'email':'მეილი',
            'mobile':'მობილური',
            'position':'თანამდებობა'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select:'
        self.fields['mobile'].required = False