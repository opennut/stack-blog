from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from questions.models import Question, Answer
from django.views.generic import DetailView, CreateView, FormView
from django.contrib.auth.models import User
from questions.forms import AnsForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class QuestionDetailView(DetailView):
	model = Question
	slug_url_kwarg = "id"
	slug_field = "pk"
	fields = ("id", "title", "description")
	template_name = "question.html"
	context_object_name = "question"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.views += 1
		self.object.save()
		return super(QuestionDetailView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(QuestionDetailView, self).get_context_data(**kwargs)
		form = AnsForm()
		form.fields['question'].widget = forms.HiddenInput()
		form.fields["question"].initial = self.get_object().id
		context['form'] = form
		return context

@login_required
def save_answer(request):
	if request.method == "POST":
		print request.POST
		form = AnsForm(request.POST) 
		if form.is_valid():
			current = form.save(commit=False)
			current.user = request.user
			current.save()
			print current
	return HttpResponseRedirect(reverse("question_detail", args={ request.POST["question"] }))


class AnswerForm(CreateView):
	form_class = AnsForm
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AnswerForm, self).form_valid(form)

class QuestionCreateView(CreateView):
	model = Question
	fields = ("title", "description", "tags")
	template_name = "newquestion.html"
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(QuestionCreateView, self).form_valid(form)
