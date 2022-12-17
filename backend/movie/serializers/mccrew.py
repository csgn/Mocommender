# SERIALIZER

from rest_framework import serializers

from movie.models import McCrew

class McCrewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = McCrew
        fields = ['id', 'name', 'employee_id', 'department', 'job', 'gender', 'profile_path']
