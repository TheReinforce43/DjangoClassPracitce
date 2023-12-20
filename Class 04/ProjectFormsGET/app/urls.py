from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='app'),
    path('form/',views.form,name='form'),
    path('result/',views.result,name='result'),
    path('DjangoForm/',views.DjangoForm,name='DjangoForm'),
]
