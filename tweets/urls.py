from django.urls import path

from . import views

urlpatterns = [
    path("", views.tweet_list_view, name="tweets-list"),
    path("create/", views.tweet_create_view, name="tweet-create"),
    path("<int:tweet_id>/", views.tweet_detail_view, name="tweet-detail"),
    path("<int:tweet_id>/delete/", views.tweet_delete_view, name="tweet-delete"),
]
