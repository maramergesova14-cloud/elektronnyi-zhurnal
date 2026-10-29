from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.students.models import Student
from apps.catalog.models import Subject

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades", verbose_name="Студент")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="grades", verbose_name="Предмет")
    value = models.PositiveSmallIntegerField("Оценка", validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateField("Дата")
    comment = models.CharField("Комментарий", max_length=250, blank=True)
    created_at = models.DateTimeField("Создана", auto_now_add=True)

    class Meta:
        ordering = ["-date", "student"]
        verbose_name = "оценка"
        verbose_name_plural = "оценки"
        constraints = [models.CheckConstraint(condition=models.Q(value__gte=1, value__lte=5), name="grade_value_1_to_5")]

    def __str__(self):
        return f"{self.student}: {self.subject} — {self.value}"

class Attendance(models.Model):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    STATUS_CHOICES = [(PRESENT, "Присутствовал(а)"), (ABSENT, "Отсутствовал(а)"), (LATE, "Опоздал(а)")]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance_records", verbose_name="Студент")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="attendance_records", verbose_name="Предмет")
    date = models.DateField("Дата")
    status = models.CharField("Статус", max_length=10, choices=STATUS_CHOICES)
    comment = models.CharField("Комментарий", max_length=250, blank=True)

    class Meta:
        ordering = ["-date", "student"]
        verbose_name = "запись посещаемости"
        verbose_name_plural = "посещаемость"
        constraints = [models.UniqueConstraint(fields=["student", "subject", "date"], name="unique_attendance_per_day_subject")]

    def __str__(self):
        return f"{self.student}: {self.date} — {self.get_status_display()}"
