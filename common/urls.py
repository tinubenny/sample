from django.urls import path
from . import views
app_name='common'

urlpatterns=[
    path('',views.common_home,name='index'),
    path('admin_login',views.common_admin_login,name='admin'),
    path('student_login',views.common_student_login,name='student'),
    path('teacher_login',views.common_teacher_login,name='teacher'),
    
]