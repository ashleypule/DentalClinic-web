# Generated by Django 5.0.6 on 2024-07-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_alter_appointment_doctor_alter_appointment_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='service',
        ),
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(default=''),
        ),
    ]