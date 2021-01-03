from rest_framework import viewsets
from rest_framework.response import Response
from itertools import chain
from .models import ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity
from .serializers import (ProjectCreatedActivitySerializer, ProjectEditedActivitySerializer,
                          PostCreatedActivitySerializer, PostEditedActivitySerializer)


class ActivityViewSet(viewsets.ViewSet):
    """
    TODO Docs
    """

    def list(self, request):
        """
        TODO Docs
        """
        serializer_data = [
            ProjectCreatedActivitySerializer(ProjectCreatedActivity.objects.all(), many=True).data,
            ProjectEditedActivitySerializer(ProjectEditedActivity.objects.all(), many=True).data,
            PostCreatedActivitySerializer(PostCreatedActivity.objects.all(), many=True).data,
            PostEditedActivitySerializer(PostEditedActivity.objects.all(), many=True).data
        ]

        for i in range(len(serializer_data)):
            if not serializer_data:
                continue

            serializer_data[i] = map(lambda x: dict(x), serializer_data[i])

        result_list = sorted(
            chain.from_iterable(data for data in serializer_data if data is not None),
            key=lambda x: x['datetime_created'],
            reverse=True
        )

        return Response(result_list)
