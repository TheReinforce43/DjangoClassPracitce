from . models import StudentModel
from django import forms 


class StudentForm(forms.ModelForm):

    class Meta:
        model=StudentModel
        # fields='__all__'
        # fields=['Roll','Name','Qualification']
        exclude=['Address']

        labels={
            'Name':'Student Name',
            'Roll':'Student Roll',
            'Qualification':'Student Qualification'
        }

        help_texts={
            'Name':'Student Name help text',
            'Roll':'Student Roll help text',
            'Qualification':'Student Qualification help text'
        }

        # widgets={

        #     'Roll':forms.PasswordInput()
        # }
