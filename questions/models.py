from django.db import models
from tags.models import Tag
from django.contrib.auth.models import User
from markupfield.fields import MarkupField
from django.utils.text import slugify
from django.utils.translation import gettext as _

class Question(models.Model):
	id = models.SlugField(max_length=200, primary_key=True, blank=False, null=False)
	title = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Titulo'))
	user = models.ForeignKey(User, blank=False, null=False, verbose_name=_("Usuario"))
	date = models.DateTimeField(blank=False, null=False, verbose_name=_('Fecha'))
	description = MarkupField(default_markup_type="markdown", blank=False, null=False, verbose_name=_('Descripcion'))
	tags = models.ManyToManyField(Tag,)
	views = models.IntegerField(default=0)
	voted = models.IntegerField(default=0)
	estatus = models.BooleanField(blank=False, null=False, default=True)

	class Meta:
		verbose_name = _("Pregunta")
		verbose_name_plural = _('Preguntas')
	
	def __unicode__(self):
		return self.title

	def save(self, **kwargs):
		if not self.id:
			self.id = slugify(self.title)
		super(Question, self).save(**kwargs)

class Answer(models.Model):
	user = models.ForeignKey(User, blank=False, null=False, verbose_name=_("Usuario"))
	question = models.ForeignKey(Question, blank=False, null=False, verbose_name=_("Pregunta"))
	date = models.DateTimeField(blank=False, null=False, verbose_name=_('Fecha'), auto_now=True)
	description = MarkupField(default_markup_type="markdown", blank=False, null=False, verbose_name=_('Descripcion'))
	flag = models.BooleanField(blank=False, null=False, default=False)

	class Meta:
		verbose_name = _("Respuesta")
		verbose_name_plural = _('Respuestas')

	def __unicode__(self):
		return self.question.title


class Vote_Question(models.Model):
	user = models.ForeignKey(User, blank=False, null=False, verbose_name=_("Usuario"))
	question = models.ForeignKey(Question, blank=False, null=False, verbose_name=_("Pregunta"))