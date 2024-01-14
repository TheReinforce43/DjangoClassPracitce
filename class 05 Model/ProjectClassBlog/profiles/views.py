from django.shortcuts import render,redirect
from . forms import ProfileForm

# Create your views here.

def add_profile(request):
    # return render(request,'profiles/add_profile.html')

    profileform=ProfileForm(request.POST)

    if profileform.is_valid():
        profileform.save()
        return redirect('add_profile')
    else :
        profileform=ProfileForm()
    return render(request,'profiles/add_profile.html',{'form':profileform})

