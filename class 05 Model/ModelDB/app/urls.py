from . import views 

from django.urls import path 

urlpatterns = [
    path('',views.index,name='app'),
    path('delete/<int:Roll>',views.delete_student,name='delete_std'),
]

