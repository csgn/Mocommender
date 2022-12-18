from rest_framework import serializers

from movie.models.mcgenre import McGenre


class McGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = McGenre
        fields = ['id', 'name']

