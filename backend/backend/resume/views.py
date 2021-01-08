from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ResumeOutlineSerializer
from .models import ResumeOutline


class ResumeOutlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and retrieving resume outlines.
    """
    serializer_class = ResumeOutlineSerializer
    queryset = ResumeOutline.objects.all()

    @action(detail=False, methods=['get'])
    def latest(self, request, *args, **kwargs):
        """
        A custom action which returns a serialized representation of the most recently uploaded resume and its related
        resume section objects.
        """
        serializer = ResumeOutlineSerializer(self.queryset.latest())
        return Response(serializer.data)
