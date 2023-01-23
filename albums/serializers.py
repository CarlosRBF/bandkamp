from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "user_id", "year"]

    def create(self, validated_data: dict) -> Album:
        return Album.objects.create(**validated_data)
