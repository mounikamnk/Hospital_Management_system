from django.urls import path
from app.views import *
urlpatterns=[
    path('About/',About,name='About'),
    path('',Home,name='Home'),
    path('contact/',contact,name='contact'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('index/',index,name='index'),
    path('view_Doctor/',view_Doctor,name='view_Doctor'),
    path('view_Patient/',view_Patient,name='view_Patient'),
    path('view_Appoint/',view_Appoint,name='view_Appoint'),
    path('add_Doctor/',add_Doctor,name='add_Doctor'),
    path('add_Patient/',add_Patient,name='add_Patient'),
    path('add_Appoint/',add_Appoint,name='add_Appoint'),
    path('delete_Doctor(?P<int:pid>)/',delete_Doctor,name='delete_Doctor'),
    path('delete_Patient(?P<int:pid>)/',delete_Patient,name='delete_Patient'),
    path('delete_Appoint(?P<int:pid>)/',delete_Appoint,name='delete_Appoint'),


]