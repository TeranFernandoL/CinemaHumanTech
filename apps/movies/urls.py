from django.urls import path
from .views import *

app_name = "movies"
urlpatterns = [
    path("", view=ListCreateMovieAPIView.as_view()),
    path("<int:pk>", view=RUDMoviewAPIView.as_view()),
    path("turn", view=ListCreateTurnAPIView.as_view()),
    path("turn/<int:pk>", view=RUDTurnAPIView.as_view()),
]
