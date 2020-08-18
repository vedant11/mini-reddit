from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:post_id>/vote/", views.vote, name="vote"),
    path("<int:post_id>/edit_message/", views.edit_message, name="edit_message"),
    path(
        "<int:pk>/view_message/", views.PostMessageView.as_view(), name="view_message",
    ),
]
