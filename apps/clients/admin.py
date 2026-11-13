from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user", "classroom", "student_code", "guardian_phone", "is_active")
    list_filter = ("classroom", "is_active")
    search_fields = ("user__first_name", "user__last_name", "student_code", "guardian_name")
