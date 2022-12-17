# SERIALIZER

from rest_framework import serializers

from movie.models import McCountry

class McCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = McCountry
        fields = ['id', 'name']
