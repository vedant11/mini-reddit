from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Apps included
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
