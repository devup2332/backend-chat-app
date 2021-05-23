from rest_framework import serializers
from api.models.Avatar import AvatarModel

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvatarModel
        fields = '__all__'
        