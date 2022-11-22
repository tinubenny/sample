from django.shortcuts import render

# Create your views here.
def teacher_home(request):
    return render(request,'teacher_templates/home.html')

def teacher_studentsview(request):
    return render(request,'teacher_templates/studentsview.html')

def teacher_profile(request):
    return render(request,'teacher_templates/profile.html')

def teacher_addattentance(request):
    return render(request,'teacher_templates/addattentance.html')

def teacher_activities(request):
    return render(request,'teacher_templates/activities.html')