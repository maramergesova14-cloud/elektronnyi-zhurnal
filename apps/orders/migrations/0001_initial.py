from django.db import migrations, models
import django.core.validators
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [("accounts", "0001_initial"), ("catalog", "0001_initial"), ("clients", "0001_initial")]
    operations = [
        migrations.CreateModel(name="Lesson", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("date", models.DateField(verbose_name="Дата")),
            ("start_time", models.TimeField(verbose_name="Время начала")),
            ("topic", models.CharField(max_length=255, verbose_name="Тема урока")),
            ("homework", models.TextField(blank=True, verbose_name="Домашнее задание")),
            ("classroom", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="lessons", to="catalog.classroom", verbose_name="Класс")),
            ("subject", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="lessons", to="catalog.subject", verbose_name="Предмет")),
            ("teacher", models.ForeignKey(limit_choices_to={"role__in": ["teacher", "class_teacher"]}, on_delete=django.db.models.deletion.PROTECT, related_name="lessons", to="accounts.user", verbose_name="Преподаватель")),
        ], options={"ordering": ("-date", "start_time"), "verbose_name": "Урок", "verbose_name_plural": "Уроки"}),
        migrations.CreateModel(name="Grade", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("value", models.PositiveSmallIntegerField(choices=[(2, "2"), (3, "3"), (4, "4"), (5, "5")], validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(5)], verbose_name="Оценка")),
            ("comment", models.CharField(blank=True, max_length=255, verbose_name="Комментарий")),
            ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата выставления")),
            ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="grades", to="orders.lesson", verbose_name="Урок")),
            ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="grades", to="clients.student", verbose_name="Ученик")),
            ("teacher", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="given_grades", to="accounts.user", verbose_name="Преподаватель")),
        ], options={"ordering": ("-created_at",), "verbose_name": "Оценка", "verbose_name_plural": "Оценки"}),
        migrations.CreateModel(name="Attendance", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("status", models.CharField(choices=[("present", "Присутствовал"), ("absent", "Отсутствовал"), ("late", "Опоздал"), ("excused", "Уважительная причина")], default="present", max_length=12, verbose_name="Статус")),
            ("note", models.CharField(blank=True, max_length=255, verbose_name="Примечание")),
            ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="attendance", to="orders.lesson", verbose_name="Урок")),
            ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="attendance", to="clients.student", verbose_name="Ученик")),
        ], options={"verbose_name": "Посещаемость", "verbose_name_plural": "Посещаемость"}),
        migrations.AddConstraint(model_name="grade", constraint=models.UniqueConstraint(fields=("student", "lesson"), name="unique_student_lesson_grade")),
        migrations.AddConstraint(model_name="attendance", constraint=models.UniqueConstraint(fields=("student", "lesson"), name="unique_student_lesson_attendance")),
    ]
