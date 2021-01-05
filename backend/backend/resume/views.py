from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ResumeOutlineSerializer
from .models import ResumeOutline


class ResumeOutlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and retrieving resume outlines.
    """
    serializer_class = ResumeOutlineSerializer
    queryset = ResumeOutline.objects.all()
