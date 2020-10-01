from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import *


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'address', 'dni')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'], phone=validated_data['phone'],
                                   address=validated_data['address'],
                                   dni=validated_data['dni'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(error_messages={"blank": "Este campo es obligatorio"})
    password = serializers.CharField(error_messages={"blank": "Este campo es obligatorio"})

    def validate(self, attrs):
        self.user_cache = authenticate(email=attrs["email"], password=attrs["password"])
        if not self.user_cache:
            raise serializers.ValidationError("Invalid login")
        else:
            return attrs

    def get_user(self):
        return self.user_cache


class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'phone', 'photo', 'address', 'dni')
        read_only_fields = ('id', 'email')
