# Generated by Django 3.2.6 on 2021-08-30 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0005_auto_20210830_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordss',
            name='last_vaccine_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='recordss',
            name='vaccine_certificate',
            field=models.FileField(blank=True, upload_to='certificates'),
        ),
    ]
