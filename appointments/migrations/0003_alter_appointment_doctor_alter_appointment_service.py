# Generated by Django 5.0.6 on 2024-07-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_remove_appointment_description_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.TextField(default='', max_length=255),
        ),
    ]
