from celery import shared_task
from feed.models import PostCreatedActivity, PostEditedActivity
from .models import Post


@shared_task
def new_post_created_activity(pk):
    print(f'New blog post created with primary key: {pk}')
    print('Creating related feed activity...')
    activity = PostCreatedActivity(post=Post.objects.get(pk=pk))
    activity.save()


@shared_task
def new_post_edited_activity(pk):
    print(f'Existing blog post edited with primary key: {pk}')
    print('Creating related feed activity...')
    activity = PostEditedActivity(post=Post.objects.get(pk=pk))
    activity.save()
