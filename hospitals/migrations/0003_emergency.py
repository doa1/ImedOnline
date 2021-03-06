# Generated by Django 2.1.2 on 2018-11-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_auto_20181022_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency', models.IntegerField(choices=[(0, 'ACCIDENT'), (1, 'POISONING'), (2, 'CHILD BIRTH'), (3, 'OTHER')], help_text='Kindly indicate the emergency', verbose_name='Emergency Type')),
                ('full_names', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250, null=True)),
                ('location', models.CharField(max_length=200)),
                ('nearest_clinic', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nearest Health Center')),
                ('description', models.TextField(help_text='Kindly give a brief description of this emergency', null=True, verbose_name='Brief Description')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Emergency',
                'verbose_name_plural': 'Emergencies',
                'ordering': ['-timestamp'],
            },
        ),
    ]
