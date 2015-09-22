from django.conf.urls import include, url
from django.contrib import admin
from .views import QuestionDetailView, QuestionCreateView

urlpatterns = [
    #url(r'^', "questions.views.home"),
    url(r'^newquestion/$', QuestionCreateView.as_view(), name="question_create"),
    url(r'^(?P<id>[\w-]+)/$', QuestionDetailView.as_view(), name="question_detail"),
    
]
