from django.conf.urls import include, url
from django.contrib import admin
from .views import HomeListQuestions, donate

urlpatterns = [
    #url(r'^', 'home.views.home', name="home"),
    url(r'^$', HomeListQuestions.as_view(), name="home"),
    url(r'^questions/$', HomeListQuestions.as_view(), name="home_filter"),
    url(r'^donate/$', donate, name="donate"),
]
