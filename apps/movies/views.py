from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status, filters
from .serializers import *


class ListCreateMovieAPIView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = MovieViewSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = MovieViewSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = MovieViewSerializer(obj, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class RUDMoviewAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Movie, id=self.kwargs['pk'])
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = MovieViewSerializer(obj, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListCreateTurnAPIView(generics.ListCreateAPIView):
    serializer_class = TurnSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Turn.objects.all()
        return queryset


class RUDTurnAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TurnSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Turn, id=self.kwargs['pk'])
        return obj
