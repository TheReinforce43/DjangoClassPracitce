
from django import forms


class contactForm(forms.Form):

    CHOICES= [ ('S','Small'),('M','Medium'),('L','Large')]

    name=forms.CharField(label='User Name')
    email=forms.EmailField(label='Email Address')
    RollNumber=forms.IntegerField(label='Roll Number')
    BodyWeight=forms.FloatField(label='Body Weight')
    Birthday=forms.DateField(label='Birthday')
    Appointment=forms.DateTimeField(label='Appointment')
    Check=forms.BooleanField(label='Check')
    Size=forms.ChoiceField(choices=CHOICES)

    meal=[ ('B','Banana'),('M','Mango'),('O','Orane'),('P','Pappaya')]

    MultipleMeal=forms.MultipleChoiceField(choices=meal)

    file=forms.FileField()