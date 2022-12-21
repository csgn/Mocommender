from rest_framework import serializers
from movie.serializers.mcmetadata import McMetadataSerializer

from user.models.mcuserrecommend import McUserRecommend


class McUserRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = McUserRecommend
        fields = ['id', 'user', 'movie', 'refer']
        depth = 1

