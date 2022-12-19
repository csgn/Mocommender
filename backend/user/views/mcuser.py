from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from user.models.mcuser import McUser
from user.models.mcusermovie import McUserMovie

from user.serializers.mcuser import McUserSerializer
from user.serializers.mcusermovie import McUserMovieSerializer

## USER
class McUserScaffoldAPIView(GenericAPIView):
    queryset = McUser.objects.all()
    serializer_class = McUserSerializer


class McUserListAPIView(McUserScaffoldAPIView, ListAPIView):
    ...


class McUserRetrieveAPIView(McUserScaffoldAPIView, RetrieveAPIView):
    ...

list_api_view = McUserListAPIView.as_view()
retrieve_api_view = McUserRetrieveAPIView.as_view()


## USER MOVIE
class McUserMovieScaffoldAPIView(GenericAPIView):
    queryset = McUserMovie.objects.all()
    serializer_class = McUserMovieSerializer

class McUserMovieListAPIView(McUserMovieScaffoldAPIView, ListAPIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset().filter(user=pk)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

class McUserMovieRetrieveAPIView(McUserMovieScaffoldAPIView, RetrieveAPIView):
    def get(self, request, fk, *args, **kwargs):
        queryset = self.get_queryset().filter(movie=fk)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    

list_user_movie_api_view = McUserMovieListAPIView.as_view()
retrieve_user_movie_api_view = McUserMovieRetrieveAPIView.as_view()
