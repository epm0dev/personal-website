from django.db import models


class ContactForm(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    first_name = models.CharField(
        max_length=50,
        null=False,
        default='John'
    )
    last_name = models.CharField(
        max_length=50,
        null=False,
        default='Doe'
    )
    middle_initial = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )
    email_address = models.EmailField(
        max_length=255,
        null=False,
        default='johndoe@example.com'
    )
    phone_number = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )
    message = models.TextField(
        max_length=5000,
        null=False,
        default='Message body'
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )
    sent = models.BooleanField(
        null=False,
        default=False
    )

    # Methods
    def __str__(self):
        return f'{self.first_name} {self.last_name} submitted a contact form at {self.datetime_created.time()} on ' \
               f'{self.datetime_created.date()}'
