# Generated by Django 2.1.2 on 2018-10-22 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultation',
            options={'verbose_name': 'Consultation Desk', 'verbose_name_plural': 'Consultations Desk'},
        ),
        migrations.AlterModelOptions(
            name='emergencies',
            options={'verbose_name': 'Emergencies', 'verbose_name_plural': 'Emergencies'},
        ),
        migrations.AlterField(
            model_name='consultation',
            name='any_medication',
            field=models.BooleanField(blank=True, default=False, help_text='Has the patient taken any medication before this', null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='diatery_advice',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diseases', to='diseases.Diseases'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='medical_advice',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='medication',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='other_info',
            field=models.TextField(blank=True, help_text='Other revelant information', null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='prescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='results',
            field=models.TextField(blank=True, help_text='Result of the diagnosis given as a feedback to the patient', null=True),
        ),
    ]
