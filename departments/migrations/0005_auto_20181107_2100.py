# Generated by Django 2.1.2 on 2018-11-07 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_auto_20181107_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultation',
            old_name='symptioms',
            new_name='symptoms',
        ),
    ]
