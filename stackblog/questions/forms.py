from django import forms
from django.contrib.auth.models import User
from .models import Answer, Question

class AnsForm(forms.ModelForm):
	
	class Meta:
		model = Answer
		fields = ('description','question',)
