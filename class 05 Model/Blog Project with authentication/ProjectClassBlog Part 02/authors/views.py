from django.shortcuts import render,redirect
from . import forms 

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


# def add_author(request):
#     if request.method=='POST':

#         authorform=forms.AuthorForm(request.POST)
#         if authorform.is_valid():
#             authorform.save()
#             return redirect('home')
#     else :
#         authorform=forms.AuthorForm()

#     return render(request, 'authors/add_author.html',{'form':authorform})

def add_register(request):

    registerform=forms.register()
    if request.method=='POST':
        registerform=forms.register(request.POST)

        if registerform.is_valid():
            registerform.save()
            messages.success(request,'Account Created Successfully')
            return redirect('add_register')
     
    return render(request,'register/add_register.html',{'form':registerform,'type':'Register'})  



def UserLogin(request):

    form=AuthenticationForm()  
    if request.method=='POST':
         
        form=AuthenticationForm(request,request.POST)

        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user_object=authenticate(username=user_name, password=user_pass)

            if user_object is not None:
                    login(request,user_object)
                    messages.success(request,'User Login Successfully')
                    return redirect('UserLogin')
            else:
                 messages.warning(request,'User Login Failed!!!')
                 return redirect('add_register')

         
     
    return render(request,'register/add_register.html',{'form':form,'type':'Log in'})         
