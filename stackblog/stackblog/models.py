from django.db import models
from django.contrib.sites.models import Site

class StackBlog(models.Model):
	"""docstring for StackBlog"""
	site = models.OneToOneField(Site, verbose_name="Site", blank=False, null=False)
	
	def __init__(self, arg):
		super(StackBlog, self).__init__()
		self.arg = arg
		

class Language()