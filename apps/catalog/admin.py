from django.contrib import admin
from .models import AcademicYear, ClassRoom, Subject

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "is_current")
    list_filter = ("is_current",)

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "class_teacher")
    list_filter = ("year",)
    search_fields = ("name",)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("name",)
