# SERIALIZER

from rest_framework import serializers

from movie.models import McCast

class McCastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = McCast
        fields = ['id', 'name', 'actor_id', 'gender', 'cast_id', 'cast_character', 'cast_order', 'profile_path']
