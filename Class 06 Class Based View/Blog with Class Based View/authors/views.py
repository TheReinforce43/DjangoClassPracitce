from django.shortcuts import render,redirect
from . import forms 

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
from django.contrib.auth.views import LoginView,LogoutView 
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import generic 
# Create your views here.


def add_author(request):
    if request.method=='POST':

        authorform=forms.AuthorForm(request.POST)
        if authorform.is_valid():
            authorform.save()
            return redirect('home')
    else :
        authorform=forms.AuthorForm()

    return render(request, 'authors/add_author.html',{'form':authorform})


def add_register(request):

    register_form=forms.RegistrationForm()    

    if request.method=='POST':
        register_form=forms.RegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return redirect('register')
    
    return render(request,'register/add_register.html',{'form':register_form,'type':'Registration'})        



def user_login(request):
    login_form=AuthenticationForm()
    if request.method=='POST':
        login_form=AuthenticationForm(request,request.POST)

        if login_form.is_valid():
            user_name=login_form.cleaned_data['username']
            user_pass=login_form.cleaned_data['password']

            user_verify=authenticate(username=user_name, password=user_pass)

            if user_verify is  not None:
                login(request,user_verify)
                messages.success(request,'Login successfully')
                return redirect('profile')
            else:
                messages.success(request,'Account Information Incorrect')
                return redirect('register')
    return render(request,'register/add_register.html',{'form':login_form,'type':'Log In'})

def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def profile(request):
    # data=Post.objects.all()
    data=Post.objects.filter(author=request.user)
    return render(request,'register/profile.html',{'data':data})


@login_required
def edit_profile(request):
    
    if request.method=='POST':
        profile_form=forms.ChangeUserData(request.POST,instance=request.user)

        if profile_form.is_valid():
            messages.success(request,'Edit Profile Succcessfully')
            profile_form.save()
            return redirect('profile')
    else:
        profile_form=forms.ChangeUserData(instance=request.user)
    return render(request,'register/updated_profile.html',{'form':profile_form})

@login_required
def pass_change(request):

    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Change Successfully')
            return redirect('profile')
    
    else :
        form=PasswordChangeForm(user=request.user)

    return render(request,'register/pass_change.html',{'form':form})


# Class Based View 


class UserLoginViw(LoginView):

    template_name='register/add_register.html'
    # success_url=reverse_lazy('profile')

    def form_valid(self,form):
        messages.success(self.request,'Login successfully!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid login')
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Log In'
        return context
    def get_success_url(self):
        return reverse_lazy('profile')


@method_decorator(login_required,name='dispatch')
class LogoutView(generic.View):
    def get(self,request):
        logout(request)
        return redirect('home')
        
    