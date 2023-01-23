from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
