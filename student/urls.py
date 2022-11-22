from django.urls import path
from . import views
app_name='student'

urlpatterns=[
    path('home',views.student_home,name='home'),
    path('profile',views.student_profile,name='profile'),
    path('attentance',views.student_attentance,name='attentance'),
]