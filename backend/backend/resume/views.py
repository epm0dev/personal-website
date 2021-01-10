from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ResumeSerializer
from .models import Resume


class ResumeOutlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and retrieving resumes.
    """
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    @action(detail=False, methods=['get'])
    def latest(self, request, *args, **kwargs):
        """
        A custom action which returns a serialized representation of the most recently uploaded resume, its related
        resume section objects, and those section's related resume subsection objects.
        """
        serializer = ResumeSerializer(self.queryset.latest())
        return Response(serializer.data)
