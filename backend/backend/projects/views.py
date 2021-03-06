from rest_framework import viewsets
from rest_framework.response import Response
from django.http.response import Http404
from .serializers import ProjectSerializer, ProjectDetailSerializer, KeywordSerializer
from .models import Project, DisplayCategory, Keyword


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and retrieving projects.
    """

    def get_queryset(self):
        """
        A method which dynamically determines the viewset's queryset, allowing for filtering of projects based on their
        display category. Project objects are filtered by specifying a category with a query parameter when requesting
        projects.

        :returns: The dynamically chosen queryset for listing and retrieving project objects from.
        """
        category = self.request.query_params.get('category', None)

        if self.action == 'retrieve' or category is None:
            return Project.objects.all()
        elif category == 'featured':
            return Project.featured.all()
        elif category == 'general':
            return Project.general.all()
        elif category == 'archived':
            return Project.archived.all()

        raise Http404

    def get_serializer_class(self):
        """
        A method which dynamically determines the serializer class to use for project objects depending on the action
        of a request. If a specific project object is being retrieved, use the serializer class which returns more of
        project's fields, otherwise (namely for the list action) use the less detailed project serializer class.

        :returns: The serializer class to use when serializing and deserializing project objects.
        """
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    """
    API endpoint for reading and writing keyword objects.
    """
    serializer_class = KeywordSerializer
    queryset = Keyword.objects.all()
