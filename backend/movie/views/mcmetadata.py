from django.db.models import query
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from movie.models.mcmetadata import McMetadata
from movie.serializers.mcmetadata import McMetadataSerializer

from stop_words import get_stop_words


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class McMetadataScaffoldAPIView(GenericAPIView):
    queryset = McMetadata.objects.all()
    serializer_class = McMetadataSerializer

    def get_paginated_queryset(self, queryset):
        serializer = self.get_serializer(queryset, many=True)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

        return serializer


class McMetadataListAPIView(McMetadataScaffoldAPIView, ListAPIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        # query params
        genre = request.query_params.get('genre')
        popularity = request.query_params.get('popularity')
        runtime = request.query_params.get('runtime')
        release_date = request.query_params.get('release_date')
        limit = request.query_params.get('limit')
        q = request.query_params.get('q')


        if genre:
            queryset = queryset.filter(genre__in=[genre])


        if release_date:
            from datetime import datetime

            r = list(map(lambda x: datetime.strptime(x, '%Y-%m-%d'), release_date.split(',')))
            if len(r) == 1:
                r.append(datetime.now())

            queryset = queryset.filter(release_date__range=r)

        if q:
            from django.db.models import Q 
            stop_words = get_stop_words('en')
            a = set(map(str.lower, q.split(' '))) - set(stop_words)
            for i in a:
                queryset = queryset.filter(Q(title__icontains=i) | Q(overview__icontains=i))

        if popularity:
            ordering = ''
            
            if popularity == 'asc':
                ordering = ''
            elif popularity == 'desc':
                ordering = '-'

            queryset = queryset.order_by(ordering + 'popularity')

        if runtime:
            _, r = runtime.split(',')

            match _:
                case '<':
                    queryset = queryset.filter(runtime__lt=r)
                case '>':
                    queryset = queryset.filter(runtime__gt=r)
                case '>=':
                    queryset = queryset.filter(runtime__gte=r)
                case '<=':
                    queryset = queryset.filter(runtime__lte=r)

        if limit:
            queryset = queryset[:int(limit)]

        return Response(self.get_paginated_queryset(queryset).data)


class McMetadataRetrieveAPIView(McMetadataScaffoldAPIView, RetrieveAPIView):
    ...


list_api_view = McMetadataListAPIView.as_view()
retrieve_api_view = McMetadataRetrieveAPIView.as_view()
