from celery import shared_task


@shared_task
def new_resume_updated_activity(pk):
    """
    TODO Docs
    """
    print(f'New resume outline created with primary key: {pk}')
    print('Creating related feed activity...')

    # TODO Create new feed activity object


@shared_task
def check_for_new_resume_version():
    """
    TODO Docs
    """
    print('Checking for new version of resume...')

    # TODO Check static/media directory for new version of resume
