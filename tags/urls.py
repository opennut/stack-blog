from django.conf.urls import include, url
from django.contrib import admin
from .views import TagsListView, TagCreateView

urlpatterns = [
    url(r'^$', TagsListView.as_view(), name="tags_list"),
    url(r'^create/$', TagCreateView.as_view(), name="tag_create"),
]
