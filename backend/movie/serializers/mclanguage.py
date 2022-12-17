# SERIALIZER

from rest_framework import serializers

from movie.models import McLanguage

class McLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = McLanguage
        fields = ['id', 'name']
