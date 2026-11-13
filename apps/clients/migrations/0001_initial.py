from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [("accounts", "0001_initial"), ("catalog", "0001_initial")]
    operations = [
        migrations.CreateModel(name="Student", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("student_code", models.CharField(blank=True, max_length=30, unique=True, verbose_name="Личный номер")),
            ("birth_date", models.DateField(blank=True, null=True, verbose_name="Дата рождения")),
            ("address", models.CharField(blank=True, max_length=255, verbose_name="Адрес")),
            ("guardian_name", models.CharField(blank=True, max_length=200, verbose_name="ФИО представителя")),
            ("guardian_phone", models.CharField(blank=True, max_length=30, verbose_name="Телефон представителя")),
            ("is_active", models.BooleanField(default=True, verbose_name="Обучается")),
            ("classroom", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="students", to="catalog.classroom", verbose_name="Класс")),
            ("user", models.OneToOneField(limit_choices_to={"role": "student"}, on_delete=django.db.models.deletion.CASCADE, related_name="student_profile", to="accounts.user", verbose_name="Учётная запись")),
        ], options={"ordering": ("classroom__name", "user__last_name", "user__first_name"), "verbose_name": "Ученик", "verbose_name_plural": "Ученики"}),
    ]
