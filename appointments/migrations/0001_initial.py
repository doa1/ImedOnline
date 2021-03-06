# Generated by Django 2.1.2 on 2018-10-24 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospitals', '0002_auto_20181022_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, help_text='Patient Email', max_length=254, null=True)),
                ('location', models.CharField(blank=True, help_text='Patient location', max_length=200, null=True)),
                ('appointment_type', models.IntegerField(choices=[(0, 'CONSULTATION'), (1, 'CHECK UP'), (2, 'DIAGNOSTICS')])),
                ('severity_level', models.IntegerField(choices=[(0, 'MILD'), (1, 'HIGH'), (2, 'EMERGENCY')])),
                ('book_date', models.DateTimeField()),
                ('is_seen', models.BooleanField(default=False, help_text='Whether the patient has been attended to or not!!')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_appointments', to='hospitals.Hospital')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'ordering': ['-created', 'patient_name'],
            },
        ),
    ]
