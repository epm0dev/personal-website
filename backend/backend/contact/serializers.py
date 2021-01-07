from rest_framework import serializers
from .models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    """
    A serializer for the ContactForm model which includes all of its fields.
    """
    class Meta:
        model = ContactForm
        fields = [
            'first_name', 'last_name', 'middle_initial', 'email_address', 'phone_number', 'message', 'datetime_created',
            'sent'
        ]
