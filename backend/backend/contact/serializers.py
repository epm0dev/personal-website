from rest_framework import serializers
from .models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    """
    TODO Docs
    """

    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'middle_initial', 'email_address', 'phone_number', 'message']
