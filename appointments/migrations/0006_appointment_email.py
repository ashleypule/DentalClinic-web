# Generated by Django 5.0.2 on 2024-08-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_alter_appointment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
    ]