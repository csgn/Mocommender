# SERIALIZER

from rest_framework import serializers

from movie.models import McCompany

class McCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = McCompany
        fields = ['id', 'name']
