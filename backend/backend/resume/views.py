from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ResumeOutlineSerializer
from .models import ResumeOutline


class ResumeOutlineViewSet(viewsets.ModelViewSet):
    """
    TODO Docs
    """
    serializer_class = ResumeOutlineSerializer
    queryset = ResumeOutline.objects.all()
