from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from .serializers import ResumeSerializer
from .models import Resume


class PassthroughRenderer(renderers.BaseRenderer):
    """
    A custom renderer class which returns data as-is.

    https://stackoverflow.com/a/51936269
    """
    media_type = ''
    format = ''

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Override the render method to simply return the data itself.
        """
        return data


class ResumeViewSet(viewsets.ModelViewSet):
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

    @action(detail=False, methods=['get'], url_path='latest/download', renderer_classes=(PassthroughRenderer,))
    def download_latest(self, *args, **kwargs):
        """
        A custom action which returns a file response containing the latest resume version in PDF format.

        https://stackoverflow.com/a/51936269
        """
        resume = self.queryset.latest()
        file_handle = resume.pdf.open()

        res = FileResponse(file_handle, content_type='application/pdf')
        res['Content-Length'] = resume.pdf.size
        res['Content-Disposition'] = 'attachment; filename=Ethan_Mancini_Resume.pdf'

        return res
