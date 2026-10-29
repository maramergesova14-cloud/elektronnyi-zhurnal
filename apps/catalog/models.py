from django.db import models

class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=120, unique=True)
    teacher_name = models.CharField("Преподаватель", max_length=150, blank=True)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "предмет"
        verbose_name_plural = "предметы"

    def __str__(self):
        return self.name
