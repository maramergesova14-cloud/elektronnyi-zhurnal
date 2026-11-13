from django.contrib import admin
from .models import Lesson, Grade, Attendance

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("date", "start_time", "classroom", "subject", "teacher", "topic")
    list_filter = ("date", "classroom", "subject", "teacher")
    search_fields = ("topic", "homework")

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "lesson", "value", "teacher", "created_at")
    list_filter = ("value", "lesson__subject", "lesson__date", "lesson__classroom")
    search_fields = ("student__user__last_name", "student__user__first_name", "comment")

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "lesson", "status")
    list_filter = ("status", "lesson__date", "lesson__classroom")
    search_fields = ("student__user__last_name",)
