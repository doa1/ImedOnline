# Generated by Django 2.1.2 on 2018-11-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_appointment_date_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_seen',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
