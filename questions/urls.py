from django.conf.urls import include, url
from django.contrib import admin
from .views import QuestionDetailView, QuestionCreateView, AnswerForm, save_answer, votating_pos, votating_neg, cerrar_pregunta, abrir_pregunta, resp_optima, elm_pregunta, elm_respuesta, update_question, update_answer
from django.views.decorators.http import require_http_methods, require_POST

urlpatterns = [
    url(r'^newquestion/$', QuestionCreateView.as_view(), name="question_create"),
    url(r'^answer/$', require_POST(AnswerForm.as_view()), name='answer'),
    url(r'^answer/save/$', save_answer, name='answer_save'),
    url(r'^(?P<id>[\w-]+)/$', QuestionDetailView.as_view(), name="question_detail"),
    url(r'^(?P<id>[\w-]+)/voteps/$',votating_pos, name = 'vote_positive'),
    url(r'^(?P<id>[\w-]+)/voteng/$',votating_neg, name = 'vote_negative'),
    url(r'^opt/(?P<id>[\w-]+)/$',resp_optima, name = 'respuesta_optima'),
    url(r'^deletequestion/(?P<id>[\w-]+)/$',elm_pregunta, name = 'eliminar_pregunta'),
    url(r'^deleteanswer/(?P<id>[\w-]+)/$',elm_respuesta, name = 'eliminar_respuesta'),
    url(r'^updatequestion/(?P<pk>[\w-]+)/$',update_question.as_view(), name = 'editar_pregunta'),
    url(r'^updateanswer/(?P<pk>[\w-]+)/$',update_answer.as_view(), name = 'editar_respuesta'),
    url(r'^openquestion/(?P<id>[\w-]+)/$',abrir_pregunta, name = 'abrir_pregunta'),
    url(r'^closequestion/(?P<id>[\w-]+)/$',cerrar_pregunta, name = 'cerrar_pregunta'),
    
]
