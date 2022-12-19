from rest_framework import serializers

from user.models.mcuser import McUser


class McUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = McUser
        fields = ['id', 'username', 'is_active']

