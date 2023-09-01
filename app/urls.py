from django.urls import path
from app.views import *
urlpatterns=[
    path('About/',About,name='About'),
    path('',Home,name='Home'),
    path('contact/',contact,name='contact'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('Index/',Index,name='Index'),
    path('View_Doctor/',View_Doctor,name='View_Doctor'),
    path('View_Patient/',View_Patient,name='View_Patient'),
    path('View_Appoint/',View_Appoint,name='View_Appoint'),
    path('Add_Doctor/',Add_Doctor,name='Add_Doctor'),
    path('Add_Patient/',Add_Patient,name='Add_Patient'),
    path('Add_Appoint/',Add_Appoint,name='Add_Appoint'),
    path('Delete_Doctor(?P<int:pid>)/',Delete_Doctor,name='Delete_Doctor'),
    path('Delete_Patient(?P<int:pid>)/',Delete_Patient,name='Delete_Patient'),
    path('Delete_Appoint(?P<int:pid>)/',Delete_Appoint,name='Delete_Appoint'),


]