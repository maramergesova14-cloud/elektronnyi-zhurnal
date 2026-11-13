from django.db import migrations


def ensure_user_profile_fields(apps, schema_editor):
    """Add profile columns only when they are missing from an existing database.

    The initial migration in clean installations already contains these fields.
    Some earlier local databases, however, recorded 0001 before the fields were
    added to it. This migration safely supports both database states.
    """
    User = apps.get_model("accounts", "User")
    table_name = User._meta.db_table
    connection = schema_editor.connection

    if table_name not in connection.introspection.table_names():
        return

    with connection.cursor() as cursor:
        existing_columns = {
            column.name
            for column in connection.introspection.get_table_description(cursor, table_name)
        }

    for field_name in ("middle_name", "phone"):
        field = User._meta.get_field(field_name)
        if field.column not in existing_columns:
            schema_editor.add_field(User, field)
            existing_columns.add(field.column)


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_add_middle_name_and_phone"),
    ]

    operations = [
        migrations.RunPython(ensure_user_profile_fields, migrations.RunPython.noop),
    ]
