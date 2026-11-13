from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [("accounts", "0001_initial")]
    operations = [
        migrations.CreateModel(name="AcademicYear", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=20, unique=True, verbose_name="Учебный год")),
            ("start_date", models.DateField(verbose_name="Начало")),
            ("end_date", models.DateField(verbose_name="Окончание")),
            ("is_current", models.BooleanField(default=False, verbose_name="Текущий")),
        ], options={"ordering": ("-start_date",), "verbose_name": "Учебный год", "verbose_name_plural": "Учебные годы"}),
        migrations.CreateModel(name="Subject", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=100, unique=True, verbose_name="Предмет")),
            ("short_name", models.CharField(blank=True, max_length=20, verbose_name="Краткое название")),
        ], options={"ordering": ("name",), "verbose_name": "Предмет", "verbose_name_plural": "Предметы"}),
        migrations.CreateModel(name="ClassRoom", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=10, unique=True, verbose_name="Класс")),
            ("class_teacher", models.ForeignKey(blank=True, limit_choices_to={"role__in": ["teacher", "class_teacher"]}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="managed_classes", to="accounts.user", verbose_name="Классный руководитель")),
            ("year", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="classes", to="catalog.academicyear", verbose_name="Учебный год")),
        ], options={"ordering": ("name",), "verbose_name": "Класс", "verbose_name_plural": "Классы"}),
    ]
