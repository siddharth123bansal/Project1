# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AttendanceStudents(models.Model):
    rollno = models.ForeignKey('Student', models.DO_NOTHING, db_column='rollno', blank=True, null=True)
    courses = models.ForeignKey('Courses', models.DO_NOTHING, blank=True, null=True)
    faculties = models.ForeignKey('Faculty', models.DO_NOTHING, blank=True, null=True)
    dates = models.DateField(db_column='Dates', blank=True, null=True)  # Field name made lowercase.
    p_a = models.CharField(db_column='P/A', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'attendance_students'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Courses(models.Model):
    course_id = models.IntegerField(db_column='Course_id', primary_key=True)  # Field name made lowercase.
    course_name = models.CharField(db_column='Course_Name', max_length=100)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=5)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courses'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Student(models.Model):
    student_id = models.IntegerField(db_column='Student_Id', primary_key=True)  # Field name made lowercase.
    studentname = models.CharField(db_column='StudentName', max_length=255)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=5)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=5)  # Field name made lowercase.
    year = models.TextField(db_column='YEAR')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'student'


class Studentcourse(models.Model):
    stu = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'studentcourse'
