from django.conf.urls import include, url
from django.contrib import admin
from .views import QuestionDetailView, QuestionCreateView, AnswerForm
from django.views.decorators.http import require_http_methods, require_POST

urlpatterns = [
    url(r'^newquestion/$', QuestionCreateView.as_view(), name="question_create"),
    url(r'^answer/$', require_POST(AnswerForm.as_view()), name='answer'),
    url(r'^(?P<id>[\w-]+)/$', QuestionDetailView.as_view(), name="question_detail"),
]
