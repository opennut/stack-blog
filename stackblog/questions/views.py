from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from questions.models import Question
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User

class QuestionDetailView(DetailView):
	model = Question
	slug_url_kwarg = "id"
	slug_field = "pk"
	#success_url = reverse("home")
	fields = ("id", "title", "description")
	template_name = "question.html"
	context_object_name = "question"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.views += 1
		self.object.save()
		return super(QuestionDetailView, self).get(request, *args, **kwargs)


class QuestionCreateView(CreateView):
	model = Question
	fields = ("id", "title", "description", "tags")
	template_name = "newquestion.html"
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(QuestionCreateView, self).form_valid(form)

