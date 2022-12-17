# VIEW

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from movie.models import McCrew
from movie.serializers import McCrewSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class McCrewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = McCrew.objects.all()
    serializer_class = McCrewSerializer
    pagination_class = StandardResultsSetPagination


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        data = serializer.data
        count = len(data)

        body = {
            "count": count,
            "data": data 
        }

        return Response(body)
