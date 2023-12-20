from django import  forms 
from django.core import validators


class contactForm(forms.Form):

    CustomerName=forms.CharField(label='Customer Name', max_length=70, required=False)
    Email=forms.EmailField(label='Email',initial='@gmail.com')
    Message=forms.CharField(widget=forms.Textarea,max_length=1000)
    BirthDay=forms.DateField(label='Birth Day',widget=forms.DateInput(attrs={'type':'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],
                                                                       message='allowed File pdf or png files')])
    # Appoinment=forms.DateTimeInput(widget=forms.DateInput(attrs={'type':'datetime-local'}))


# Without using Validators 

# class StudentForm(forms.Form):

#     name=forms.CharField(label='Student Name',widget=forms.TextInput)
#     email=forms.CharField(label='Email',widget=forms.EmailInput)

    # def clean_name(self):
    #     valName=self.cleaned_data['name']
    #     if len(valName) <10:
    #         raise forms.ValidationError('Enter At least 10 characters')
    #     else :
    #         return valName
    
    # def clean_email(self):
    #     valEmail=self.cleaned_data['email']
    #     if '@gmail.com' not in valEmail:
    #         raise forms.ValidationError('Your gmail not maintain gmail address rules')
    #     else :
    #         return valEmail

    # def clean(self):
    #     cleaned_data=super().clean()
    #     valName=cleaned_data['name']
    #     valEmail=cleaned_data['email']

    #     if len(valName) < 10:
    #         raise forms.ValidationError('Please Enter at least 10 characters')
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError('Your Email not maintain Standard Email')



class StudentForm(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(25,message='Enter maximum 10 characters'),
                                                            validators.MinLengthValidator(10,message='Enter minimum 10 characters')])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a Valid Email')])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message='Enter age at most 34'),
                                                                 validators.MinValueValidator(24,message='Enter age at least 24')])
    
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],
                                                                       message='Enter pdf file extension')])
    
class PasswordValidation(forms.Form):

    name=forms.CharField(widget=forms.TextInput)
    InitalPassword=forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        
        cleaned_data=super().clean()
        val_name=cleaned_data['name']
        val_InitialPassword=cleaned_data['InitalPassword']
        val_ConfirmPassword=cleaned_data['ConfirmPassword']

        if len(val_name)<4 :
            raise forms.ValidationError('Please Enter your full Name!!')
        if val_InitialPassword != val_ConfirmPassword:
            raise forms.ValidationError('Password Invalid, please Re-entered')
