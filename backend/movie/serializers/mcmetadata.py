# SERIALIZER

from rest_framework import serializers

from movie.models import McMetadata

class McMetadataSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    cast = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    crew = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = McMetadata
        fields = ['id', 'imdb_id', 'genre', 'cast', 'crew', 'title', 'overview', 'popularity', 'release_date', 'runtime', 'vote_count', 'vote_average', 'poster_path']



