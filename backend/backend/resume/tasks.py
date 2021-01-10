from celery import shared_task
from feed.models import ResumeUploadedActivity
from .models import Resume


@shared_task
def new_resume_uploaded_activity(pk):
    """
    A Celery task which creates a new activity feed object and is executed when a new resume object is created.
    """
    print(f'New resume outline created with primary key: {pk}')
    print('Creating related feed activity...')
    activity = ResumeUploadedActivity(resume=Resume.objects.get(pk=pk))
    activity.save()
