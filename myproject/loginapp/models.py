from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(db_column='Student_Id', primary_key=True)  # Field name made lowercase.
    studentname = models.CharField(db_column='StudentName', max_length=255)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=5)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=5)  # Field name made lowercase.
    year = models.TextField(db_column='YEAR')
    def _str_(self):
        return self.studentname
    class Meta:
        managed = False
        db_table = 'student'

class AttendanceStudents(models.Model):
    rollno = models.ForeignKey('Student', models.DO_NOTHING, db_column='rollno', blank=True, null=True)
    courses = models.ForeignKey('Courses', models.DO_NOTHING, blank=True, null=True)
    faculties = models.ForeignKey('Faculty', models.DO_NOTHING, blank=True, null=True)
    dates = models.DateField(db_column='Dates', blank=True, null=True)  # Field name made lowercase.
    p_a = models.CharField(db_column='P/A', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'attendance_students'

class Courses(models.Model):
    course_id = models.IntegerField(db_column='Course_id', primary_key=True)  # Field name made lowercase.
    course_name = models.CharField(db_column='Course_Name', max_length=100)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=5)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courses'

class Faculty(models.Model):
    faculty_id = models.IntegerField(primary_key=True)
    faculty_name = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(db_column='Branch', max_length=3, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'faculty'


class FacultyCourses(models.Model):
    fid = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='FID', blank=True, null=True)  # Field name made lowercase.
    cid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='CID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculty_courses'

class Studentcourse(models.Model):
    stu = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'studentcourse'        