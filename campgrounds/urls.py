from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = "campgrounds"

urlpatterns = [
    path("individual/<int:pk>/",campground,name="individual"),
    path("comment/<int:pk>",comment,name="comment"),
    path("add/",AddCampground.as_view(),name="add")
]
