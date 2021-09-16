from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from homepage.models import Favorites
from api.serializers import FavoritesSerializer


class FavoritesViewSet(ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()


@api_view(['POST', ])
def api_add_favorite_view(request):
    if request.method == 'POST':
        serializer = FavoritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
