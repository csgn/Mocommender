# VIEW

from rest_framework import viewsets
from rest_framework.response import Response

from movie.models import McCountry
from movie.serializers import McCountrySerializer



class McCountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = McCountry.objects.all()
    serializer_class = McCountrySerializer


    def list(self, request, *args, **kwargs):
        try:
            data = McCountrySerializer(self.get_queryset(),
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
