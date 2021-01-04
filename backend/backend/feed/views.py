from rest_framework import viewsets
from rest_framework.response import Response
from django.http.response import HttpResponseNotFound
from itertools import chain
from math import ceil
from .models import ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity
from .serializers import (ProjectCreatedActivitySerializer, ProjectEditedActivitySerializer,
                          PostCreatedActivitySerializer, PostEditedActivitySerializer)


class ActivityViewSet(viewsets.ViewSet):
    """
    TODO Docs
    """
    count = 0
    num_pages = 1
    results_per_page = 20

    def get_paginated_response(self, results, page):
        """
        TODO Docs
        """
        res = {'count': self.count}

        if page == self.num_pages:
            res['next'] = None
        else:
            res['next'] = f'http://localhost:8000/api/feed/?page={page + 1}'

        if page == 1:
            res['previous'] = None
        else:
            res['previous'] = f'http://localhost:8000/api/feed/?page={page - 1}'

        page_start = self.results_per_page * (page - 1)
        page_end = self.results_per_page * page

        res['results'] = results[page_start:page_end]

        return Response(res)

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

        results = sorted(
            chain.from_iterable(data for data in serializer_data if data is not None),
            key=lambda x: f"{x['date_created']} {x['time_created']}",
            reverse=True
        )

        self.count = len(results)
        self.num_pages = ceil(self.count / self.results_per_page)

        if 'page' not in request.query_params.keys():
            return self.get_paginated_response(results, 1)
        else:
            page = int(request.query_params['page'])
            if page > 0 and page <= self.num_pages:
                return self.get_paginated_response(results, page)
            else:
                return HttpResponseNotFound('<h1>Page not found</h1>')
