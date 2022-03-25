from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = "campgrounds"

urlpatterns = [
    path("add/",add,name="add"),
    path("individual/",ind,name="ind"),
    path("comment/",comment,name="comment"),

]
