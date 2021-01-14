from django.db import models


class ContactForm(models.Model):
    """
    A model for contact form submissions. Contact forms objects contain the name and contact information of the person
    who submitted the form, a message, the date and time the form was submitted, and a field which represents whether
    or not the form has been relayed in a daily digest email.
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

    # Properties
    @property
    def formatted(self):
        """
        TODO Docs
        """
        if self.middle_initial:
            name = f'{self.first_name} {self.middle_initial}. {self.last_name}'
        else:
            name = f'{self.first_name} {self.last_name}'

        out = f'{name}\nEmail: {self.email_address}\n'

        if self.phone_number:
            out += f'Phone: {self.phone_number}\n\n{self.message}\n'
        else:
            out += f'\n{self.message}\n'

        return out



    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a contact form object to contain the first and last name of
        the person who submitted the form as well as the time and date the form was submitted.
        """
        return f'{self.first_name} {self.last_name} submitted a contact form at {self.datetime_created.time()} on ' \
               f'{self.datetime_created.date()}'
