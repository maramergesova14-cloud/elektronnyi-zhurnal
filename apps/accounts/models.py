from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Администратор"
        TEACHER = "teacher", "Преподаватель"
        CLASS_TEACHER = "class_teacher", "Классный руководитель"
        STUDENT = "student", "Ученик"

    role = models.CharField("Роль", max_length=20, choices=Role.choices, default=Role.STUDENT)
    middle_name = models.CharField("Отчество", max_length=150, blank=True)
    phone = models.CharField("Телефон", max_length=30, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.get_full_name() or self.username
