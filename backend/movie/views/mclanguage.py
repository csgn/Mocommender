# VIEW

from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination

from movie.models import McLanguage
from movie.serializers import McLanguageSerializer


# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 20


class McLanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = McLanguage.objects.all()
    serializer_class = McLanguageSerializer
#     pagination_class = StandardResultsSetPagination


    def list(self, request, *args, **kwargs):
        try:
            data = McLanguageSerializer(self.get_queryset(),
                                        context={'request':request},
                                        many=True).data
        except Exception as e: 
            return Response({
                "error": str(e)
            }, status=500)

        count = len(data)

        body = {
            "count": count,
            "data": data 
        }

        return Response(body)
