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
    API endpoint for listing all types of feed activity in one paginated list that is ordered by the date and time at
    which they were created.
    """
    count = 0
    num_pages = 1
    results_per_page = 20

    def get_paginated_response(self, results, page):
        """
        A method which builds a paginated response for the specified page of the results.
        """
        res = {'count': self.count}

        # Handle the edge case of the last page being requested
        if page == self.num_pages:
            res['next'] = None
        else:
            res['next'] = f'http://localhost:8000/api/feed/?page={page + 1}'

        # Handle the edge case of the first page being requested
        if page == 1:
            res['previous'] = None
        else:
            res['previous'] = f'http://localhost:8000/api/feed/?page={page - 1}'

        # Calculate the starting and ending indices for the slice of results to return
        page_start = self.results_per_page * (page - 1)
        page_end = self.results_per_page * page

        # Add the slice of results to the response and return it
        res['results'] = results[page_start:page_end]
        return Response(res)

    def list(self, request):
        """
        A method which defines the list action for the view set. It combines all of the serialized activity objects into
        one list to return as a paginated response.
        """
        serializer_data = [
            ProjectCreatedActivitySerializer(ProjectCreatedActivity.objects.all(), many=True).data,
            ProjectEditedActivitySerializer(ProjectEditedActivity.objects.all(), many=True).data,
            PostCreatedActivitySerializer(PostCreatedActivity.objects.all(), many=True).data,
            PostEditedActivitySerializer(PostEditedActivity.objects.all(), many=True).data
        ]

        # Map each set of serialized activity objects to python dictionaries
        for i in range(len(serializer_data)):
            if not serializer_data:
                continue
            serializer_data[i] = map(lambda x: dict(x), serializer_data[i])

        # Chain together all of the serializer data and sort by the date and time each activity was created
        results = sorted(
            chain.from_iterable(data for data in serializer_data if data is not None),
            key=lambda x: f"{x['date_created']} {x['time_created']}",
            reverse=True
        )

        # Update the count of activity objects and the number of pages available
        self.count = len(results)
        self.num_pages = ceil(self.count / self.results_per_page)

        # Return the first page of serialized activity objects if no page was specified
        if 'page' not in request.query_params.keys():
            return self.get_paginated_response(results, 1)
        else:
            page = int(request.query_params['page'])

            # Return the requested page of serialized activity objects, or that the page was not found if the specified
            # page number is outside of the valid range
            if page > 0 and page <= self.num_pages:
                return self.get_paginated_response(results, page)
            else:
                return HttpResponseNotFound('<h1>Page not found</h1>')
