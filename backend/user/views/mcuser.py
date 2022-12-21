from datetime import datetime
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import status
from rest_framework.response import Response
from movie.models.mcmetadata import McMetadata

from user.models.mcuser import McUser
from user.models.mcusermovie import McUserMovie
from user.models.mcuserrecommend import McUserRecommend

from user.serializers.mcuser import McUserSerializer
from user.serializers.mcusermovie import McUserMovieSerializer
from user.serializers.mcuserrecommend import McUserRecommendSerializer

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

    def put(self, request, pk, fk, *args, **kwargs):
        queryset = self.get_queryset().filter(movie=fk)

        if len(queryset) == 0:
            new_um = McUserMovie.objects.create(user=McUser.objects.filter(pk=pk)[0],
                                                movie=McMetadata.objects.filter(pk=fk)[0],
                                                is_played=True,
                                                is_recommended=False,
                                                is_liked=False,
                                                is_saved=False,
                                                play_runtime=0.0,
                                                play_date=datetime.today().strftime('%Y-%m-%d'))
            new_um.save()
            serializer = self.get_serializer(new_um)
            Response(serializer.data)

        else:
            for i in queryset:
                i.is_played = True
                i.save()

        return Response({"message": "Already exist"})


    

list_user_movie_api_view = McUserMovieListAPIView.as_view()
retrieve_user_movie_api_view = McUserMovieRetrieveAPIView.as_view()



## USER RECOMMEND
class McUserRecommendScaffoldAPIView(GenericAPIView):
    queryset = McUserRecommend.objects.all()
    serializer_class = McUserRecommendSerializer


class McUserRecommendListAPIView(McUserRecommendScaffoldAPIView, ListAPIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset().filter(user=pk)
        limit = request.query_params.get('limit')
        popularity = request.query_params.get('popularity')

        if limit:
            queryset = queryset[:int(limit)]


        if popularity:
            ordering = ''
            
            if popularity == 'asc':
                ordering = ''
            elif popularity == 'desc':
                ordering = '-'

            queryset = queryset.order_by(ordering + 'movie__popularity')



        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class McUserRecommendRetrieveAPIView(McUserRecommendScaffoldAPIView, RetrieveAPIView):
    def get(self, request, fk, *args, **kwargs):
        queryset = self.get_queryset().filter(movie=fk)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    

list_user_recommend_api_view = McUserRecommendListAPIView.as_view()
retrieve_user_recommend_api_view = McUserRecommendRetrieveAPIView.as_view()

"""
create table if not exists McUserRecommend (
     id             serial      not null
    ,user_id        integer     not null
    ,movie_id       integer     not null
    ,refer_id       integer     not null


    ,CONSTRAINT fk_ref_user
        FOREIGN KEY (user_id)
            REFERENCE McUser (id)
    ,CONSTRAINT fk_ref_movie
        FOREIGN KEY (movie_id)
            REFERENCE McMetadata (id)
    ,CONSTRAINT fk_ref_refer
        FOREIGN KEY (refer_id)
            REFERENCE McMetadata (id)

    ,PRIMARY KEY (id)
)
"""
