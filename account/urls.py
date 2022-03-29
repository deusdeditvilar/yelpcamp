from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = "account"

urlpatterns = [
    path("",landing,name="landing"),
    path("home/",home,name="home"),
    path("signup/",SignUpView.as_view(),name="signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/home/"), name="logout"),
]
