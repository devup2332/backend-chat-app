from rest_framework import serializers
from api.models.Avatar import Avatar

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'
        