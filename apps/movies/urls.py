from django.urls import path
from .views import *

app_name = "cinema"
urlpatterns = [
    path("movie", view=ListCreateMovieAPIView.as_view()),
    path("movie/<int:pk>", view=RUDMoviewAPIView.as_view()),
    path("turn", view=ListCreateTurnAPIView.as_view()),
    path("turn/<int:pk>", view=RUDTurnAPIView.as_view()),
]
