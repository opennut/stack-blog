from django.db import models
from tags.models import Tag
from django.contrib.auth.models import User
from markupfield.fields import MarkupField

class Question(models.Model):
	user = models.ForeignKey(User, blank=False, null=False, verbose_name="Usuario")
	date = models.DateTimeField(blank=False, null=False, verbose_name='Fecha', auto_now=True)
	title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Titulo')
	description = MarkupField(default_markup_type="markdown", blank=False, null=False, verbose_name='Descripcion')
	tags = models.ManyToManyField(Tag,)
	views = models.IntegerField(default=0)
	estatus = models.BooleanField(blank=False, null=False, default=True)

	class Meta:
		verbose_name = "Question"
		verbose_name_plural = 'Questions'
	
	def __unicode__(self):
		return self.title


class Answer(models.Model):
	user = models.ForeignKey(User, blank=False, null=False, verbose_name="Usuario")
	question = models.ForeignKey(Question, blank=False, null=False, verbose_name="Question")
	date = models.DateTimeField(blank=False, null=False, verbose_name='Fecha', auto_now=True)
	description = MarkupField(default_markup_type="markdown", blank=False, null=False, verbose_name='Descripcion')
	flag = models.BooleanField(blank=False, null=False, default=True)

	class Meta:
		verbose_name = "Answer"
		verbose_name_plural = 'Answer'