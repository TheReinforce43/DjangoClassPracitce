from . import views 

from django.urls import path 


urlpatterns = [
    path('',views.App_home),
    path('contact',views.Contact),
    path('about',views.About),
]
