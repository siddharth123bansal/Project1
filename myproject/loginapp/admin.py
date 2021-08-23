from django.contrib import admin
from .models import Student,Faculty,Courses,FacultyCourses,Studentcourse,AttendanceStudents

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Courses)
admin.site.register(FacultyCourses)
admin.site.register(Studentcourse)
admin.site.register(AttendanceStudents)

# Register your models here.
