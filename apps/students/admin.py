from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "group_name", "email", "is_active")
    list_filter = ("group_name", "is_active")
    search_fields = ("first_name", "last_name", "email")
