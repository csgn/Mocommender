from rest_framework import serializers

from movie.models.mcmetadata import McMetadata


class McMetadataSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = McMetadata
        fields = ['id', 'imdb_id', 'title', 'overview', 'popularity', 'release_date', 'runtime', 'vote_average', 'vote_count', 'genre']

