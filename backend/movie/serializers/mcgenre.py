# SERIALIZER

from rest_framework import serializers

from movie.models import McGenre

class McGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = McGenre
        fields = ['id', 'name']
