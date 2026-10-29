from django.db import models

class Student(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    group_name = models.CharField("Группа", max_length=30, db_index=True)
    email = models.EmailField("Электронная почта", blank=True)
    is_active = models.BooleanField("Обучается", default=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "студент"
        verbose_name_plural = "студенты"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.group_name})"
