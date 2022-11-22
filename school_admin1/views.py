from django.shortcuts import render

# Create your views here.
def school_admin1_home(request):
    return render(request,'school_admin1_templates/home.html')

def school_admin1_addstudent(request):
    return render(request,'school_admin1_templates/addstudent.html')

def school_admin1_studentattentance(request):
    return render(request,'school_admin1_templates/studentattentance.html')

def school_admin1_studentsview(request):
    return render(request,'school_admin1_templates/studentsview.html')