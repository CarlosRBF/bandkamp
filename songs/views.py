from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from rest_framework import generics

from .models import Song
from .serializers import SongSerializer

from albums.models import Album


class SongView(
    generics.ListCreateAPIView,
    PageNumberPagination,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album=self.kwargs["album_id"])

    def perform_create(self, serializer):
        albumID = get_object_or_404(Album, id=self.kwargs["album_id"])
        serializer.save(album=albumID)
