from celery import shared_task
from .models import ContactForm
from django.core.mail import send_mail


@shared_task
def send_contact_form_digest():
    """
    TODO Docs
    """
    unsent = ContactForm.objects.all().filter(sent=False)
    print(f'Found {len(unsent)} unsent contact forms; building email digest message...')

    subject = f'New Contact Form Digest: {len(unsent)} new messages'
    body = ''

    if len(unsent) == 0:
        body = 'See you tomorrow!'
        return

    for form in unsent:
        body += f'{form.formatted}\n\n'

    status = send_mail(
        subject,
        body,
        'Personal Website Contact Form Digest <contact@epm0dev.me>',
        ['epmancin@ncsu.edu']
    )

    if status:
        unsent.update(sent=True)