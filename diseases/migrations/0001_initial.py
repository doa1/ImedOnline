# Generated by Django 2.1.2 on 2018-10-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(verbose_name=((0, 'PEDIATRIC'), (1, 'GYNECOLOGY'), (2, 'SEXUAL HEALTH'), (3, 'COUGH & ALLERGY'), (4, 'SKIN & RASHES'), (5, 'CHRONIC'), (6, 'OTHER')))),
                ('name', models.CharField(max_length=250)),
                ('effects', models.TextField(help_text='States the effects of every disease on the human body')),
            ],
        ),
    ]
