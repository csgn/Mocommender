# VIEW

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from movie.models import McMetadata
from movie.serializers import McMetadataSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class McMetadataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = McMetadata.objects.all()
    serializer_class = McMetadataSerializer
    pagination_class = StandardResultsSetPagination


    def list(self, request, *args, **kwargs):
        params_ids = request.query_params.get('ids')
        queryset = self.filter_queryset(self.get_queryset())

        if params_ids:
            queryset = queryset.filter(pk__in=params_ids.split(','))


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
