# Generated by Django 3.1.4 on 2021-01-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210102_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='message',
            field=models.TextField(default='Message body', max_length=5000),
        ),
    ]
