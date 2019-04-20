# Generated by Django 2.1.2 on 2018-10-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases',
            name='category',
            field=models.IntegerField(choices=[(0, 'PEDIATRIC'), (1, 'GYNECOLOGY'), (2, 'SEXUAL HEALTH'), (3, 'COUGH & ALLERGY'), (4, 'SKIN & RASHES'), (5, 'CHRONIC'), (6, 'OTHER')]),
        ),
        migrations.AlterField(
            model_name='diseases',
            name='name',
            field=models.CharField(choices=[('USA', (('gm', 'General Motors'), ('tesla', 'Tesla'), ('ford', 'Ford'))), ('South Korea', (('kia', 'Kia Motors'), ('hyundai', 'Hyundai Motors'))), ('Japan', (('nissan', 'Nissan Motors'), ('honda', 'Honda Motors'), ('toyota', 'Toyota Motors')))], max_length=250),
        ),
    ]
