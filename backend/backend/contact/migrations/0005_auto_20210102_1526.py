# Generated by Django 3.1.4 on 2021-01-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contactform_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='middle_initial',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]