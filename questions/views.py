from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from questions.models import Question, Answer, Vote_Question
from django.views.generic import DetailView, CreateView, FormView, UpdateView
from django.contrib.auth.models import User
from questions.forms import AnsForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.translation import gettext as _

class QuestionDetailView(DetailView):
	model = Question
	slug_url_kwarg = "id"
	slug_field = "pk"
	fields = ("id", "title", "description")
	template_name = "question.html"
	context_object_name = "question"

	def get(self, request, *args, **kwargs):
		date = self.get_object().date
		self.object = self.get_object()
		self.object.views += 1
		self.object.date = date
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
		form = AnsForm(request.POST) 
		if form.is_valid():
			current = form.save(commit=False)
			current.user = request.user
			current.date = datetime.datetime.now()
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
		form.instance.date = datetime.datetime.now()
		return super(QuestionCreateView, self).form_valid(form)


def votating_pos(request, id):
	user = request.user
	y = Question.objects.get(pk=id)
	c= Vote_Question.objects.filter(user=user, question=y)
	if(c.count()>0):
		print "nice try"
	else:
		y.voted += 1
		x = Vote_Question(user = user, question = y)
		y.save()
		x.save()
	return HttpResponseRedirect(reverse("question_detail", args={ y.title }))


def votating_neg(request, id):
	user = request.user
	print user.id
	y = Question.objects.get(pk=id)
	c= Vote_Question.objects.filter(user=user, question=y)
	if(c.count()>0):
		print "nice try"
	else:
		y.voted -= 1
		x = Vote_Question(user = user, question = y)
		y.save()
		x.save()
	return HttpResponseRedirect(reverse("question_detail", args={ y.title }))


def resp_optima (request, id):
	answer = Answer.objects.get(pk=id)
	question = answer.question
	user = request.user
	if(question.user == user):
		try:
			x = Answer.objects.get(question = question, flag = True)
			x.flag = False
			x.save()

		except Answer.DoesNotExist:
			x = None  

		answer.flag = True
		answer.save()

	return HttpResponseRedirect(reverse("question_detail", args={ question.id }))


def elm_pregunta(request, id):
	user = request.user
	question = Question.objects.get(pk=id)
	if (question.user == user or user.is_staff):
		question.delete()
	return HttpResponseRedirect(reverse('home'))

def elm_respuesta(request, id):
	user = request.user
	answer = Answer.objects.get(pk = id)
	question = answer.question
	if (answer.user == user or user.is_staff):
		answer.delete()
	return HttpResponseRedirect(reverse("question_detail", args={ question.title }))

class update_question (UpdateView):
	model = Question
	context_object_name = "current"
	fields = ['title', 'description', 'tags']
	template_name = 'upquestion.html'
	
	def get_success_url(self):
		return reverse('question_detail', kwargs={'id': self.object.pk})

class update_answer (UpdateView):
	model = Answer
	context_object_name = "current"
	fields = ['description']
	template_name = 'upquestion.html'

	def get_success_url(self):
		return reverse('question_detail', kwargs={'id': self.object.question.pk})

