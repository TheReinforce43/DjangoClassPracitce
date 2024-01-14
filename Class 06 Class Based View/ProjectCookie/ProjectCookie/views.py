from django.shortcuts import HttpResponse,render

def home(request):
    response=render(request,'home.html')
    response.set_cookie('name','Farhan Kabir')
    return render(request,'home.html')