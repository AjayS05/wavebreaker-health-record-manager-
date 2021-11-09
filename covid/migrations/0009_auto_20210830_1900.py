# Generated by Django 3.2.6 on 2021-08-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0008_alter_recordss_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordss',
            name='vaccine_certificate',
        ),
        migrations.AddField(
            model_name='recordss',
            name='vaccine_certificate_beneficiary_id',
            field=models.BigIntegerField(blank=True, default=1234567890123),
            preserve_default=False,
        ),
    ]
