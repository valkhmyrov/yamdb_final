from rest_framework import serializers

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('email', 'username')
        model = User


class CreateTokenSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(max_length=128, required=True)
    email = serializers.EmailField(max_length=128, required=True)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')
        model = User
