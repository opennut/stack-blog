from django import template
from ..models import Tag
from datetime import date

register = template.Library()

@register.inclusion_tag("tags/tag_side_bar.html", takes_context=True)
def tag_side_bar(context):
	tags = Tag.objects.all().order_by("name")
	return {
		"tags_side": tags,
	}


