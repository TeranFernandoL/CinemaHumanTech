from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import *


class TurnSerializer(serializers.ModelSerializer):
    schedule = serializers.TimeField()

    class Meta:
        model = Turn
        fields = '__all__'

    def validate_schedule(self, value):
        if Turn.objects.filter(schedule=value).exists():
            raise serializers.ValidationError("Este turno ya existe")
        return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieViewSerializer(serializers.ModelSerializer):
    turns = TurnSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
