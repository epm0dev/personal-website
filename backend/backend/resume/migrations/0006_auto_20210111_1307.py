# Generated by Django 3.1.4 on 2021-01-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20210109_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='file',
            new_name='document',
        ),
        migrations.AddField(
            model_name='resume',
            name='pdf',
            field=models.FileField(default='o', upload_to='resume/'),
            preserve_default=False,
        ),
    ]
