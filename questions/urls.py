from django.conf.urls import include, url
from django.contrib import admin
from .views import QuestionDetailView, QuestionCreateView, AnswerForm, save_answer, votating_pos, votating_neg, resp_optima
from django.views.decorators.http import require_http_methods, require_POST

urlpatterns = [
    url(r'^newquestion/$', QuestionCreateView.as_view(), name="question_create"),
    url(r'^answer/$', require_POST(AnswerForm.as_view()), name='answer'),
    url(r'^answer/save/$', save_answer, name='answer_save'),
    url(r'^(?P<id>[\w-]+)/$', QuestionDetailView.as_view(), name="question_detail"),
    url(r'^(?P<id>[\w-]+)/voteps/$',votating_pos, name = 'vote_positive'),
    url(r'^(?P<id>[\w-]+)/voteng/$',votating_neg, name = 'vote_negative'),
    url(r'^opt/(?P<id>[\w-]+)/$',resp_optima, name = 'respuesta_optima')
]
