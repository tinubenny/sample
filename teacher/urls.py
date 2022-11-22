from django.urls import path
from . import views
app_name='teacher'


urlpatterns=[
    path('home',views.teacher_home,name='home'),
    path('studentsview',views.teacher_studentsview,name='stud_view'),
    path('profile',views.teacher_profile,name='profile'),
    path('addattentance',views.teacher_addattentance,name='attentance'),
    path('activities',views.teacher_activities,name='activity'),

]