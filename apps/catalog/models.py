from django.db import models

class AcademicYear(models.Model):
    title = models.CharField("Учебный год", max_length=20, unique=True)
    start_date = models.DateField("Начало")
    end_date = models.DateField("Окончание")
    is_current = models.BooleanField("Текущий", default=False)

    class Meta:
        ordering = ("-start_date",)
        verbose_name = "Учебный год"
        verbose_name_plural = "Учебные годы"

    def __str__(self):
        return self.title

class ClassRoom(models.Model):
    name = models.CharField("Класс", max_length=10, unique=True)
    year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT, related_name="classes", verbose_name="Учебный год")
    class_teacher = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, blank=True,
                                       limit_choices_to={"role__in": ["teacher", "class_teacher"]},
                                       related_name="managed_classes", verbose_name="Классный руководитель")

    class Meta:
        ordering = ("name",)
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField("Предмет", max_length=100, unique=True)
    short_name = models.CharField("Краткое название", max_length=20, blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name
