from rest_framework import serializers
from movie.serializers.mcmetadata import McMetadataSerializer

from user.models.mcusermovie import McUserMovie


class McUserMovieSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    #movie = serializers.RelatedField(source='McMetadata.title', read_only=True, many=True)

    class Meta:
        model = McUserMovie
        fields = ['id', 'user', 'movie', 'is_played', 'is_recommended', 'is_liked', 'is_saved', 'play_runtime', 'play_date']
        depth = 1

