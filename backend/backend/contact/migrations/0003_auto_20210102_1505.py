# Generated by Django 3.1.4 on 2021-01-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210102_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='message',
        ),
        migrations.AddField(
            model_name='contactform',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]