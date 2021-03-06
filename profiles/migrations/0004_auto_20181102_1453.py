# Generated by Django 2.1.2 on 2018-11-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20181022_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='specialization',
            field=models.IntegerField(choices=[(0, 'SURGEON'), (1, 'NEUROSURGEON'), (2, 'UROLOGY'), (3, 'ENT'), (4, 'OPHTHALMOLOGIST'), (5, 'GYNECOLOGIST'), (6, 'DERMATOLOGIST'), (7, 'NEUROLOGIST'), (8, 'PATHOLOGIST'), (9, 'RADIOLOGIST'), (10, 'ANESTHESIOLOGIST'), (11, 'PSYCHIATRIC'), (12, 'PEDIATRIC'), (13, 'FAMILY PRACTIONER'), (14, 'RADIATION ONCOLOGIST'), (15, 'Physical Medicine and Rehab (PM & R)'), (16, 'Emergency Medicine Physicist'), (18, 'Psychologists/Counselors'), (19, 'Podiatrists'), (20, 'Optometrists')], help_text='Your area of specialization', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qualifications',
            field=models.TextField(blank=True, null=True),
        ),
    ]
