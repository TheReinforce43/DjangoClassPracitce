from django.shortcuts import render
from . forms import contactForm
from . forms import StudentForm
from . forms import PasswordValidation

# Create your views here.


def  index(request):
    # return render(request,'app/index.html')
    if request.method=='POST':
        form=contactForm(request.POST,request.FILES)

        if form.is_valid():
            # file=form.cleaned_data['file']
            print(form.cleaned_data)
        else :
            print('Error here ',form.errors)
    else :
        form=contactForm()
    return render(request,'app/index.html',{'form':form})


def StudentData(request):

    if request.method=='POST':

        form=StudentForm(request.POST,request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    else :
        form=StudentForm()

    return render(request,'app/student.html',{'form':form}) 

def PasswordValidationProject(request):
    if request.method=='POST':
        form=PasswordValidation(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        else :
            print(form.errors)
    else:
        form=PasswordValidation()
    
    return render(request,'app/PasswordValidation.html',{'form':form})