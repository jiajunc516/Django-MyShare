from django.urls import path

from . import views

app_name = "image_app"

urlpatterns = [
    path(
        "upload/",
        views.image_upload,
        name="image_upload"
    ),
    path(
        "",
        views.image_list,
        name="image_list"
    ),
    path(
        "<int:id>/<str:slug>/",
        views.image_detail,
        name="image_detail"
    ),
    path(
        "like/<int:id>/",
        views.image_like,
        name="image_like"
    ),
    path(
        "unlike/<int:id>/",
        views.image_unlike,
        name="image_unlike"
    ),
    path(
        "tag/<str:tag_slug>/",
        views.image_list,
        name="image_list_by_tag"
    ),
    path(
        "add-tag/<int:id>/",
        views.add_tag,
        name="add_tag"
    )
]