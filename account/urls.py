from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = "account"

urlpatterns = [
    path("",landing,name="landing"),
    path("home/",home,name="home"),
    path("signup/",signup,name="signup"),
    path("login/",login,name="login"),
]
