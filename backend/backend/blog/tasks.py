from celery import shared_task
from feed.models import PostCreatedActivity, PostEditedActivity
from .models import Post


@shared_task
def new_post_created_activity(pk):
    """
    A Celery task which creates a new activity feed object and is executed when a new blog post object is created.
    """
    print(f'New blog post created with primary key: {pk}')
    print('Creating related feed activity...')
    activity = PostCreatedActivity(post=Post.objects.get(pk=pk))
    activity.save()


@shared_task
def new_post_edited_activity(pk):
    """
    A Celery task which creates a new activity feed object and is executed when an existing blog post object is edited.
    """
    print(f'Existing blog post edited with primary key: {pk}')
    print('Creating related feed activity...')
    activity = PostEditedActivity(post=Post.objects.get(pk=pk))
    activity.save()
