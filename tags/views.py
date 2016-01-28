from django.shortcuts import render
from tags.models import Tag
from django.views.generic import ListView,CreateView
from django.db.models import Q
from django.utils.translation import gettext as _

class TagsListView(ListView):
	model = Tag
	template_name = "tags.html"
	context_object_name = "tag_list"
	ordering = "name"

	def get_queryset(self):
		qs = super(TagsListView, self).get_queryset()
		filter_name = self.request.GET.get('tag', None)
		if filter_name != None:
			qs = qs.filter(Q(name__contains=filter_name) | Q(description__contains=filter_name))
		return qs

class TagCreateView(CreateView):
	model = Tag
	fields = ("name", "description")
	template_name = "newtag.html"
	success_url = '/'
