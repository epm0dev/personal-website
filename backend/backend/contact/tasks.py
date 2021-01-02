from celery import shared_task


@shared_task
def send_contact_form_digest():
    print('Sending daily contact form digest')
