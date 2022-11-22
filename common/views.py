from django.shortcuts import render

# Create your views here.
def common_home(request):
    return render(request,'common_templates/home.html')

def common_admin_login(request):
    return render(request,'common_templates/admin_login.html')

def common_student_login(request):
    return render(request,'common_templates/student_login.html')

def common_teacher_login(request):
    return render(request,'common_templates/teacher_login.html')