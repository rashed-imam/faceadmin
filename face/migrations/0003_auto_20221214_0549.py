# Generated by Django 3.2 on 2022-12-14 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_service_employee_attandance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attandance',
            new_name='Attendance',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='employe',
            new_name='employee',
        ),
    ]