from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path("login", view=LoginAPIView.as_view()),
    path("create", view=CreateUserAPIView.as_view()),
    path("listcreate", view=ListCreateUserAPIView.as_view()),
    path("", view=RUDUserAPIView.as_view()),
]
