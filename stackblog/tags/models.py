from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False, unique=True)
    description = models.TextField()
    status = models.BooleanField(blank=False, null=False, default=True)
    
    class Meta:
    	verbose_name = "Tag"
    	verbose_name_plural = 'Tags'
    
    def __unicode__(self):
        return self.name
