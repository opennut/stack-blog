from django.shortcuts import render
from django.views.generic import ListView
from questions.models import Question


class HomeListQuestions(ListView):
	model = Question
	template_name = "home.html"
	paginate_by = 10
	context_object_name = "question_list"
		

def home(request):
	questions = Question.objects.all()
	return render(request, 'home.html', {
		"questions":questions
		})

