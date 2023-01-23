from django.urls import path

from . import views
from songs import views as song_views

urlpatterns = [
    path("albums/", views.AlbumView.as_view()),
    path("albums/<int:album_id>/songs/", song_views.SongView.as_view()),
]
