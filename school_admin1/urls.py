from django.urls import path
from . import views
app_name='school_admin1'

urlpatterns=[
    path('home',views.school_admin1_home,name='home'),
    path('addstudent',views.school_admin1_addstudent,name='add_stud'),
    path('studentattentance',views.school_admin1_studentattentance,name='stud_attentance'),
    path('studentsview',views.school_admin1_studentsview,name='stud_view'),
]