from rest_framework import viewsets
from rest_framework import permissions
from .models import ContactForm
from .serializers import ContactFormSerializer


class ContactFormViewSet(viewsets.ModelViewSet):
    """
    TODO Docs
    """
    serializer_class = ContactFormSerializer
    queryset = ContactForm.objects.all()
    permission_classes = [permissions.AllowAny]
