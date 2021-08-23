from django.http import HttpResponse
from django.shortcuts import render
from .models import Student,Faculty,Courses,FacultyCourses,Studentcourse,AttendanceStudents
mobilenumber = 2000
def studentlogin(request):
    if request.method == 'POST':
        mobilenumber = request.POST.get('mobilenumber')
        print (mobilenumber)
    return render(request, 'student_login.html', {})

def teacherlogin(request):
    return render(request, 'teacher_login.html', {})

def about(request):
    return render(request, 'about_us.html', {})

def dashboard(request):
        return render(request, 'student_dashboard.html', {})
def generateotp(request):
        return render(request, 'teacher_dashboard.html', {})
def myprofile(request):
    data = Student.objects.all()
    
    return render(request, 'profile.html', {"messages":data})
# Create your views here.
