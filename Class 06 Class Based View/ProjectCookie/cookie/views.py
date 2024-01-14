from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.


def add_cookie(request):
    response=render(request,'cookie.html')
    response.set_cookie('Name','Adnan Rana')
    response.set_cookie('Name','Sohel Sabbir',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name=request.COOKIES.get('Name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})


def delete_cookie(request):
    response=render(request,'delete.html')
    response.delete_cookie('Name')
    return response


def set_session(request):

    data={
        'name':'Rahim Uddin',
        'age':35,
        'language':'Bangla',
        'Institution':'DUET'
    }
    request.session.update(data)
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    return render(request, 'home.html')

def get_session(request):

    name=request.session.get('name')
    age=request.session.get('age')
    return render(request,'get_session.html',{'name':name, 'age':age})

def delete_session(request):
    request.session.flush()
    return render(request,'delete.html')
