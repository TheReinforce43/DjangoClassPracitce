from django.urls import path
from . import views


urlpatterns = [
    # path('',views.add_cookie,name='cookie'),
    path('',views.set_session,name='cookie'),
    path('session/',views.get_session,name='session'),
    path('get_cookie/',views.get_cookie,name='get_cookie'),
    # path('delete/',views.delete_cookie,name='delete'),
    path('delete_session/',views.delete_session,name='delete'),
]
