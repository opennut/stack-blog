from django.db import models
from django.utils.translation import gettext as _

class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=25, blank=False, null=False, unique=True)
    description = models.TextField()
    status = models.BooleanField(blank=False, null=False, default=True)
    
    class Meta:
    	verbose_name = _("Tag")
    	verbose_name_plural = _('Tags')
    
    def __unicode__(self):
        return self.name
