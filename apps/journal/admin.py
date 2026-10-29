from django.contrib import admin
from .models import Attendance, Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("date", "student", "subject", "value")
    list_filter = ("date", "subject", "value")
    search_fields = ("student__first_name", "student__last_name", "subject__name")
    date_hierarchy = "date"

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("date", "student", "subject", "status")
    list_filter = ("date", "subject", "status")
    search_fields = ("student__first_name", "student__last_name", "subject__name")
    date_hierarchy = "date"
