from django.urls import path 

from . import views 


urlpatterns = [
    path('register/',views.add_register,name='add_register'),
    path('login/',views.UserLogin,name='UserLogin'),
]
