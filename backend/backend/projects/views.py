from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProjectSerializer, ProjectDetailSerializer, KeywordSerializer
from .models import Project, DisplayCategory


class ProjectViewSet(viewsets.ModelViewSet):
    """
    TODO Docs
    """

    def get_queryset(self):
        """
        TODO Docs
        """
        category = self.request.query_params.get('category', None)

        if category is not None:
            if category == 'featured':
                return Project.featured.all()
            elif category == 'general':
                return Project.general.all()
            elif category == 'archived':
                return Project.archived.all()

        # TODO HTTP Error here?
        return Project.objects.all()

    def get_serializer_class(self):
        """
        TODO Docs
        """
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    """
    TODO Docs
    """
    serializer_class = KeywordSerializer
