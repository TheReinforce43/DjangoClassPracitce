from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/',views.StudentData,name='student'),
    path('password/',views.PasswordValidationProject,name='password'),
    
]
