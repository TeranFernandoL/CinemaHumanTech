from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path("/signin", view=LoginAPIView.as_view()),
    path("/signup", view=CreateUserAPIView.as_view()),
    path("/profile", view=RUDUserAPIView.as_view()),
]
