from django.shortcuts import render
from django.views.generic import ListView
from questions.models import Question
from django.db.models import Q

class HomeListQuestions(ListView):
	model = Question
	template_name = "home.html"
	paginate_by = 10
	ordering = "-date"
	context_object_name = "question_list"
		
	def get_queryset(self):
		qs = super(HomeListQuestions, self).get_queryset()
		filter_name = self.request.GET.get('tag', None)
		if filter_name != None:
			qs = qs.filter(tags__in=[filter_name])
		filter_name = self.request.GET.get('search', None)
		if filter_name != None:
			qs = qs.filter(Q(title__contains=filter_name) | Q(description__contains=filter_name))
		return qs