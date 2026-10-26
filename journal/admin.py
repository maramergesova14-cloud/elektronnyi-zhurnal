from django.contrib import admin
from .models import Attendance, Grade, Student, Subject


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "class_name", "email")
    search_fields = ("first_name", "last_name", "class_name")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher_name")
    search_fields = ("name", "teacher_name")


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "value", "date")
    list_filter = ("subject", "value", "date")


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "date", "status")
    list_filter = ("status", "subject", "date")
