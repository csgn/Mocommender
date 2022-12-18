from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from movie.models.mcgenre import McGenre
from movie.serializers.mcgenre import McGenreSerializer



class McGenreScaffoldAPIView(GenericAPIView):
    queryset = McGenre.objects.all()
    serializer_class = McGenreSerializer


class McGenreListAPIView(McGenreScaffoldAPIView, ListAPIView):
    ...


class McGenreRetrieveAPIView(McGenreScaffoldAPIView, RetrieveAPIView):
    ...


mcgenre_list_api_view = McGenreListAPIView.as_view()
mcgenre_retrieve_api_view = McGenreRetrieveAPIView.as_view()
