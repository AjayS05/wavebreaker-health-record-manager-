# Generated by Django 3.2.6 on 2021-08-30 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0004_auto_20210830_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recordss',
            old_name='covi_date',
            new_name='covid_test_date',
        ),
        migrations.RenameField(
            model_name='recordss',
            old_name='position',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='recordss',
            old_name='l_vax',
            new_name='last_vaccine_date',
        ),
        migrations.RenameField(
            model_name='recordss',
            old_name='no_vax',
            new_name='no_of_vaccines_taken',
        ),
        migrations.RenameField(
            model_name='recordss',
            old_name='certificate',
            new_name='vaccine_certificate',
        ),
    ]
