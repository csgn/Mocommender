# SERIALIZER

from rest_framework import serializers

from user.models import McUser, McUserMovie


class McUserSerializer(serializers.HyperlinkedModelSerializer):
    user_movie = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = McUser
        fields = ['id', 'username', 'is_active', 'user_movie']
