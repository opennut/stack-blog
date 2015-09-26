from django.conf.urls import include, url
from django.contrib import admin
from .views import TagsListView

urlpatterns = [
    url(r'^$', TagsListView.as_view(), name="tags_list"),
]
