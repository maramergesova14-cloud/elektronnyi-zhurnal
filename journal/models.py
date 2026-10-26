from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Student(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    class_name = models.CharField("Класс", max_length=20)
    email = models.EmailField("Электронная почта", blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "ученик"
        verbose_name_plural = "ученики"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.class_name})"


class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=100, unique=True)
    teacher_name = models.CharField("Преподаватель", max_length=150, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "предмет"
        verbose_name_plural = "предметы"

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="grades", verbose_name="ученик"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="grades", verbose_name="предмет"
    )
    value = models.PositiveSmallIntegerField(
        "оценка", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    date = models.DateField("дата")
    comment = models.CharField("комментарий", max_length=250, blank=True)

    class Meta:
        ordering = ["-date", "student"]
        verbose_name = "оценка"
        verbose_name_plural = "оценки"

    def __str__(self):
        return f"{self.student}: {self.subject} — {self.value}"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ("present", "Присутствовал(а)"),
        ("absent", "Отсутствовал(а)"),
        ("late", "Опоздал(а)"),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="attendance_records", verbose_name="ученик"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="attendance_records", verbose_name="предмет"
    )
    date = models.DateField("дата")
    status = models.CharField("статус", max_length=10, choices=STATUS_CHOICES)

    class Meta:
        ordering = ["-date", "student"]
        verbose_name = "запись посещаемости"
        verbose_name_plural = "посещаемость"

    def __str__(self):
        return f"{self.student}: {self.date} — {self.get_status_display()}"
