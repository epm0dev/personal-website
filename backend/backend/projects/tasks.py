from celery import shared_task
from django.apps import apps
from feed.models import ProjectCreatedActivity, ProjectEditedActivity
from projects.models import Project


@shared_task
def new_project_created(pk):
    print(f'New project created with primary key: {pk}')
    print('Creating related feed activity')
    activity = ProjectCreatedActivity(project=Project.objects.get(pk=pk))
    activity.save()


@shared_task
def project_edited(pk):
    print(f'Existing project edited with primary key: {pk}')
    print('Creating related feed activity')
    activity = ProjectEditedActivity(project=Project.objects.get(pk=pk))
    activity.save()
