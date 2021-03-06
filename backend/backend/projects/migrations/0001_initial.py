# Generated by Django 3.1.4 on 2020-12-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ['-word'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('description_verbose', models.TextField(default='A long-form description for this project has yet to '
                                                                 'be added.', max_length=10000)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_changed', models.DateTimeField(auto_now=True)),
                ('phase', models.PositiveSmallIntegerField(
                    choices=[(1, 'Design'), (2, 'Implementation'), (3, 'Integration'), (4, 'Maintenance')],
                    default=1)),
                ('category', models.PositiveIntegerField(
                    choices=[(1, 'Featured'), (2, 'General'), (3, 'Archived')],
                    default=2)
                 ),
                ('_keywords', models.ManyToManyField(related_name='projects', to='projects.Keyword')),
            ],
            options={
                'ordering': ['phase', '-datetime_changed'],
                'get_latest_by': 'datetime_created',
                'unique_together': {('description', 'description_verbose')},
            },
        ),
        migrations.AddField(
            model_name='keyword',
            name='_projects',
            field=models.ManyToManyField(related_name='keywords', to='projects.Project'),
        ),
    ]
