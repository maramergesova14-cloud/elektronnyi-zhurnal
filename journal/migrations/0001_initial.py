# Generated for the electronic journal models.
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=100, verbose_name="Фамилия")),
                ("class_name", models.CharField(max_length=20, verbose_name="Класс")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="Электронная почта")),
            ],
            options={
                "verbose_name": "ученик",
                "verbose_name_plural": "ученики",
                "ordering": ["last_name", "first_name"],
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Название предмета")),
                ("teacher_name", models.CharField(blank=True, max_length=150, verbose_name="Преподаватель")),
            ],
            options={
                "verbose_name": "предмет",
                "verbose_name_plural": "предметы",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("value", models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name="оценка")),
                ("date", models.DateField(verbose_name="дата")),
                ("comment", models.CharField(blank=True, max_length=250, verbose_name="комментарий")),
                ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="grades", to="journal.student", verbose_name="ученик")),
                ("subject", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="grades", to="journal.subject", verbose_name="предмет")),
            ],
            options={
                "verbose_name": "оценка",
                "verbose_name_plural": "оценки",
                "ordering": ["-date", "student"],
            },
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(verbose_name="дата")),
                ("status", models.CharField(choices=[("present", "Присутствовал"), ("absent", "Отсутствовал"), ("late", "Опоздал")], max_length=10, verbose_name="статус")),
                ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="attendance_records", to="journal.student", verbose_name="ученик")),
                ("subject", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="attendance_records", to="journal.subject", verbose_name="предмет")),
            ],
            options={
                "verbose_name": "запись посещаемости",
                "verbose_name_plural": "посещаемость",
                "ordering": ["-date", "student"],
            },
        ),
    ]
