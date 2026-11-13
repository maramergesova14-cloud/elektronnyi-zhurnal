from django.db import models
from apps.accounts.models import User
from apps.catalog.models import ClassRoom

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile",
                                limit_choices_to={"role": User.Role.STUDENT}, verbose_name="Учётная запись")
    classroom = models.ForeignKey(ClassRoom, on_delete=models.PROTECT, related_name="students", verbose_name="Класс")
    student_code = models.CharField("Личный номер", max_length=30, unique=True, blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    address = models.CharField("Адрес", max_length=255, blank=True)
    guardian_name = models.CharField("ФИО представителя", max_length=200, blank=True)
    guardian_phone = models.CharField("Телефон представителя", max_length=30, blank=True)
    is_active = models.BooleanField("Обучается", default=True)

    class Meta:
        ordering = ("classroom__name", "user__last_name", "user__first_name")
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        return f"{self.user} ({self.classroom})"
