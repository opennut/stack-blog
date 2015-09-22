from django.db import models
from tags.models import Tag
from django.contrib.auth.models import User
from markupfield.fields import MarkupField
from django.utils.text import slugify

class Question(models.Model):
	id = models.SlugField(max_length=200, primary_key=True, blank=False, null=False)
	title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Titulo')
	user = models.ForeignKey(User, blank=False, null=False, verbose_name="Usuario")
	date = models.DateTimeField(blank=False, null=False, verbose_name='Fecha', auto_now=True)
	description = MarkupField(default_markup_type="markdown", blank=False, null=False, verbose_name='Descripcion')
	tags = models.ManyToManyField(Tag,)
	views = models.IntegerField(default=0)
	estatus = models.BooleanField(blank=False, null=False, default=True)

	class Meta:
		verbose_name = "Question"
		verbose_name_plural = 'Questions'
	
	def __unicode__(self):
		return self.title

	def save(self, **kwargs):
		if not self.id:
			self.id = slugify(self.title)
		super(Question, self).save(**kwargs)

class Answer(models.Model):
	user = models.ForeignKey(User, blank=False, null=False, verbose_name="Usuario")
	question = models.ForeignKey(Question, blank=False, null=False, verbose_name="Question")
	date = models.DateTimeField(blank=False, null=False, verbose_name='Fecha', auto_now=True)
	description = MarkupField(default_markup_type="markdown", blank=False, null=False, verbose_name='Descripcion')
	flag = models.BooleanField(blank=False, null=False, default=True)

	class Meta:
		verbose_name = "Answer"
		verbose_name_plural = 'Answer'
	