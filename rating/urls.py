from django.urls import path
from . import views


urlpatterns= [
    path("upload/", views.upload_image),
    path("rank/", views.ranking),
    path("add/", views.add_thumbnail),
    path("index/",views.index),
]