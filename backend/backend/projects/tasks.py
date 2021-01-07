from celery import shared_task
from feed.models import ProjectCreatedActivity, ProjectEditedActivity
from .models import Project


@shared_task
def new_project_created_activity(pk):
    """
    TODO Docs
    """
    print(f'New project created with primary key: {pk}')
    print('Creating related feed activity...')
    activity = ProjectCreatedActivity(project=Project.objects.get(pk=pk))
    activity.save()


@shared_task
def new_project_edited_activity(pk):
    """
    TODO Docs
    """
    print(f'Existing project edited with primary key: {pk}')
    print('Creating related feed activity...')
    activity = ProjectEditedActivity(project=Project.objects.get(pk=pk))
    activity.save()
