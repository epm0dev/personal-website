# Generated by Django 3.1.4 on 2021-01-11 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20201231_1435'),
        ('blog', '0003_auto_20210102_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='projects.project'),
        ),
    ]
