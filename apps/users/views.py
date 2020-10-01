from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *

from django.utils.deprecation import MiddlewareMixin


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        token, created = Token.objects.get_or_create(user=serializer.get_user())
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class ListCreateUserAPIView(generics.ListCreateAPIView):
    serializer_class = RetrieveUserSerializer

    def get_queryset(self):
        return User.objects.filter(gender='HOMBRE')


class RUDUserAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RetrieveUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ChangePasswordAPIView(generics.GenericAPIView):
    '''Cambiar contraseña para usuario logueado'''
    permission_classes = IsAuthenticated,
    serializer_class = ChangePasswordSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={"user": request.user})
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({"detail": "OK"}, status=status.HTTP_200_OK)
