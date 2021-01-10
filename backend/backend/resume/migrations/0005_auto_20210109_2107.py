# Generated by Django 3.1.4 on 2021-01-10 02:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20210109_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'get_latest_by': ['date_uploaded', 'time_uploaded']},
        ),
        migrations.AddField(
            model_name='resume',
            name='time_uploaded',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
