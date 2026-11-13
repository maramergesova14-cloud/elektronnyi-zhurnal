from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.accounts.models import User
from apps.catalog.models import ClassRoom, Subject
from apps.clients.models import Student

class Lesson(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="lessons", verbose_name="Класс")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="lessons", verbose_name="Предмет")
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, related_name="lessons", limit_choices_to={"role__in": ["teacher", "class_teacher"]}, verbose_name="Преподаватель")
    date = models.DateField("Дата")
    start_time = models.TimeField("Время начала")
    topic = models.CharField("Тема урока", max_length=255)
    homework = models.TextField("Домашнее задание", blank=True)

    class Meta:
        ordering = ("-date", "start_time")
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.date} — {self.classroom} — {self.subject}"

class Grade(models.Model):
    class GradeValue(models.IntegerChoices):
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades", verbose_name="Ученик")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="grades", verbose_name="Урок")
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, related_name="given_grades", verbose_name="Преподаватель")
    value = models.PositiveSmallIntegerField("Оценка", choices=GradeValue.choices, validators=[MinValueValidator(2), MaxValueValidator(5)])
    comment = models.CharField("Комментарий", max_length=255, blank=True)
    created_at = models.DateTimeField("Дата выставления", auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        constraints = [models.UniqueConstraint(fields=("student", "lesson"), name="unique_student_lesson_grade")]

    def __str__(self):
        return f"{self.student}: {self.value}"

class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = "present", "Присутствовал"
        ABSENT = "absent", "Отсутствовал"
        LATE = "late", "Опоздал"
        EXCUSED = "excused", "Уважительная причина"

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance", verbose_name="Ученик")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="attendance", verbose_name="Урок")
    status = models.CharField("Статус", max_length=12, choices=Status.choices, default=Status.PRESENT)
    note = models.CharField("Примечание", max_length=255, blank=True)

    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемость"
        constraints = [models.UniqueConstraint(fields=("student", "lesson"), name="unique_student_lesson_attendance")]

    def __str__(self):
        return f"{self.student}: {self.get_status_display()}"
