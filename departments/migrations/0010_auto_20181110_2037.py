# Generated by Django 2.1.2 on 2018-11-10 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0009_auto_20181107_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='appointments.Appointment'),
        ),
    ]
