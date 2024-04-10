from django.core.validators import MinLengthValidator, MaxLengthValidator

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from .validators import username_validator, password_validator

from djoser.serializers import UserSerializer as Serializer, \
    UserCreateSerializer


class UserSerializer(Serializer):
    class Meta(Serializer.Meta):
        model = User
        fields = ['id', 'username', 'email']


class CreateUserSerializer(UserCreateSerializer):
    email = serializers.EmailField(validators=[
        UniqueValidator(message='This email is already in use',
                        queryset=User.objects.all()),
        MaxLengthValidator(limit_value=150,
                           message='Email must be shorter than 150 characters')
    ],
        required=True
    )
    username = serializers.CharField(validators=[
        UniqueValidator(message='This username is already in use',
                        queryset=User.objects.all()), username_validator],
        required=True
    )
    password = serializers.CharField(validators=[
        MinLengthValidator(
            limit_value=6,
            message='The password must be more than 6 characters'
        ),
        MaxLengthValidator(
            limit_value=20,
            message='The password must be less than 20 characters'
        ), password_validator],
        required=True, write_only=True,
    )

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'password']
