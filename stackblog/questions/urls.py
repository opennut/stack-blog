from django.conf.urls import include, url
from django.contrib import admin
from .views import QuestionDetailView, QuestionCreateView, MyFormView
from django.views.decorators.http import require_http_methods, require_POST

urlpatterns = [
    #url(r'^', "questions.views.home"),
    url(r'^newquestion/$', QuestionCreateView.as_view(), name="question_create"),
    url(r'^my_form/$', require_POST(MyFormView.as_view()), name='my_form_view_url'),
    url(r'^(?P<id>[\w-]+)/$', QuestionDetailView.as_view(), name="question_detail"),
]
