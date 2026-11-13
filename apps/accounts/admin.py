from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Дополнительно", {"fields": ("role", "middle_name", "phone")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Дополнительно", {"fields": ("role", "middle_name", "phone")}),)
    list_display = ("username", "last_name", "first_name", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
