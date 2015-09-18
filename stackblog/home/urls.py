from django.conf.urls import include, url
from django.contrib import admin
from .views import HomeListQuestions

urlpatterns = [
    #url(r'^', 'home.views.home', name="home"),
    url(r'^$', HomeListQuestions.as_view(), name="home"),
]
