from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request,'AppUrl/contact.html')

def about(request):
    return render(request,'AppUrl/about.html')

def home(request):
    return render(request,'AppUrl/home.html')